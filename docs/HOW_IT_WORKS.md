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

## Stage 3: Streaming

### What This Stage Does

Prints tokens as they arrive from the API instead of waiting for the full response.

### Request Shape

```python
stream = client.chat.completions.create(
    model=MODEL,
    max_completion_tokens=200,
    messages=[{"role": "user", "content": "Count from 1 to 10"}],
    stream=True
)
for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
```

### Response Shape

Each `chunk` has:
- `chunk.choices[0].delta.content` - the new token (or None)
- `chunk.choices[0].finish_reason` - "stop" when done

### Key Concept: Streaming

Streaming lets you show output incrementally. The `delta.content` may be `None` on some chunks - always check before printing. Token usage is typically only available in the final chunk or via a separate non-streaming call.

### Experiment to Try

Ask for a long story and watch it appear word by word. Compare the perceived speed vs. non-streaming.

## Stage 4: Structured Output

### What This Stage Does

Requests JSON output, parses it, validates against a schema, and retries once if malformed.

### Request Shape

```python
response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    response_format={"type": "json_object"}
)
```

The prompt must explicitly say the answer must be JSON.

### Response Shape

```python
text = response.choices[0].message.content  # JSON string
data = json.loads(text)                      # Parsed dict
```

### Key Concept: Structured Output

`response_format={"type": "json_object"}` tells the model to output only JSON. But models can still produce invalid JSON or miss fields. Always validate and retry.

### Key Concept: Validation and Retry

Parse with `json.loads()`, then check types and required fields. On failure, send the bad output back with a correction prompt and try once more.

### Experiment to Try

Change the schema to require a nested object. See if the model gets it right on first try or needs the retry.