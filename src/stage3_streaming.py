from common import get_client, MODEL, print_usage

def main() -> None:
    client = get_client()

    stream = client.chat.completions.create(
        model=MODEL,
        max_completion_tokens=200,
        messages=[{"role": "user", "content": "Count from 1 to 10, one number per line."}],
        stream=True
    )

    print("Streaming: ")
    collected = []
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)
            collected.append(delta)

    print("\n")
    full = "".join(collected)
    # Usage is only in the last chunk (or not at all in streaming)
    # For demo, make a non-streaming call to show usage
    response = client.chat.completions.create(
        model=MODEL,
        max_completion_tokens=200,
        messages=[{"role": "user", "content": "Count from 1 to 10, one number per line."}]
    )
    print_usage(response.usage)

if __name__ == "__main__":
    main()