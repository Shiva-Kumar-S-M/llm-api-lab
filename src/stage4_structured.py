import json
from common import get_client, MODEL, print_usage

SCHEMA_PROMPT = """Return a JSON object with exactly these fields:
{
  "name": "string",
  "age": "integer",
  "skills": ["string", ...]
}
No extra fields. No markdown. Just the JSON."""

def parse_and_validate(text: str) -> dict:
    data = json.loads(text)
    assert isinstance(data.get("name"), str), "name must be string"
    assert isinstance(data.get("age"), int), "age must be integer"
    assert isinstance(data.get("skills"), list), "skills must be list"
    for s in data["skills"]:
        assert isinstance(s, str), "each skill must be string"
    return data

def main() -> None:
    client = get_client()

    messages = [
        {"role": "system", "content": "You output only valid JSON."},
        {"role": "user", "content": SCHEMA_PROMPT}
    ]

    for attempt in range(2):
        response = client.chat.completions.create(
            model=MODEL,
            max_completion_tokens=200,
            messages=messages,
            response_format={"type": "json_object"}
        )

        text = response.choices[0].message.content
        print(f"Attempt {attempt + 1} raw:\n{text}\n")

        try:
            data = parse_and_validate(text)
            print("Parsed and validated:")
            print(json.dumps(data, indent=2))
            print_usage(response.usage)
            return
        except (json.JSONDecodeError, AssertionError) as e:
            print(f"Validation failed: {e}")
            if attempt == 0:
                messages.append({"role": "assistant", "content": text})
                messages.append({"role": "user", "content": "Invalid JSON. Fix it and return only valid JSON matching the schema."})
            else:
                print("Retries exhausted.")
                print_usage(response.usage)

if __name__ == "__main__":
    main()