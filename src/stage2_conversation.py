from common import get_client, MODEL, print_usage

def main() -> None:
    client = get_client()
    messages = []

    print("Conversation mode. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ("quit", "exit"):
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=MODEL,
            max_completion_tokens=200,
            messages=messages
        )

        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})

        print(f"Assistant: {reply}")
        print_usage(response.usage)
        print(f"Messages in history: {len(messages)}")
        print()

if __name__ == "__main__":
    main()