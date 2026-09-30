# LLM API Lab

A command-line assistant that teaches how an LLM API works, one stage at a time.

## What This Is

This project walks through five stages of using the Groq API:
1. Basic call - send one message, print reply and token usage
2. Conversation memory - keep a messages list, show the API is stateless
3. Streaming - print tokens as they arrive
4. Structured output - request JSON, parse and validate it
5. Tool use loop - tools for reading files, listing files, and calculating

Each stage builds on the previous one.

## Requirements

- Python 3.11 or higher
- A Groq API key

## Setup

```bash
cd llm-api-lab
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

## How to Run Each Stage

```bash
# Stage 1: Basic call
python src/stage1_basic.py

# Stage 2: Conversation memory
python src/stage2_conversation.py

# Stage 3: Streaming
python src/stage3_streaming.py

# Stage 4: Structured output
python src/stage4_structured.py

# Stage 5: Tool use loop
python src/stage5_tools.py
```

## Project Structure

```
llm-api-lab/
├── src/
│   ├── common.py              # Shared helpers
│   ├── stage1_basic.py        # Stage 1: Basic call
│   ├── stage2_conversation.py # Stage 2: Conversation memory
│   ├── stage3_streaming.py    # Stage 3: Streaming
│   ├── stage4_structured.py   # Stage 4: Structured output
│   └── stage5_tools.py        # Stage 5: Tool use loop
├── workspace/                 # Sample files for file tools
├── docs/
│   ├── STATE.md               # Current project state
│   ├── HOW_IT_WORKS.md        # Explanations for each stage
│   ├── PROMPT_NOTES.md        # System prompt versions
│   └── GITHUB_GUIDE.md        # Git setup guide
├── .env.example               # Environment template
├── .gitignore
├── requirements.txt
└── README.md
```

## Where to Learn More

- `docs/HOW_IT_WORKS.md` - What each stage does and key concepts
- `docs/PROMPT_NOTES.md` - System prompt versions
- `docs/STATE.md` - Current progress and how to run
- `docs/GITHUB_GUIDE.md` - Git setup instructions