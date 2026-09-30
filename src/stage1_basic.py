from common import get_client, MODEL, print_usage

def main() -> None:
    client = get_client()

    response = client.chat.completions.create(
        model=MODEL,
        max_completion_tokens=100,
        messages=[{"role": "user", "content": "Say hello in one sentence."}]
    )

    print(response.choices[0].message.content)
    print_usage(response.usage)

if __name__ == "__main__":
    main()