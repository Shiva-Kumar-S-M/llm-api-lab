# How It Works

## Stage 1: Basic Call

### What This Stage Does

Sends a single message to the Groq API and prints the reply along with token usage.

### Request Shape

```python
client.chat.completions.create(
    model=MODEL,
    max_completion_tokens=100,
    messages=[{"role": "user", "content": "Say hello in one sentence."}]
)
```

### Response Shape

```python
response.choices[0].message.content      # The reply text
response.usage.prompt_tokens             # Input tokens
response.usage.completion_tokens         # Output tokens
response.usage.total_tokens              # Total tokens used
```

### Key Concept: Tokens

A token is a piece of text - roughly 4 characters or 3/4 of a word. The API counts tokens in your input (prompt_tokens) and the model's output (completion_tokens). The total cannot exceed the model's context window.

### Key Concept: Stateless API

The API does not remember previous calls. Each request is independent. You must send the full conversation history every time if you want context.

### Experiment to Try

Change the prompt to ask a question that needs a longer answer, then increase `max_completion_tokens` to see the token counts change.

## Stage 2: Conversation Memory

### What This Stage Does

Keeps a list of messages and sends the full history with each request. Demonstrates that the API is stateless - it does not remember anything between calls.

### Request Shape

```python
messages = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there!"},
    {"role": "user", "content": "What did I just say?"}
]
response = client.chat.completions.create(
    model=MODEL,
    max_completion_tokens=200,
    messages=messages
)
```

### Response Shape

Same as Stage 1, plus the growing `messages` list.

### Key Concept: Stateless API

The API does not store conversation history. Every request must include the full message list. The `messages` list in your code is the "memory" - the API itself has none.

### Key Concept: Context Window

The total tokens (input + output) must fit within the model's context window. As the conversation grows, input tokens increase. If you exceed the limit, the request fails.

### Experiment to Try

Have a long conversation until you notice input tokens growing. Then ask "What was my first message?" - the model can answer because the full history is in the request.