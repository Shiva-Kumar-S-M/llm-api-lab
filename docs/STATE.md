# Project State

## Goal
Build a command-line assistant that teaches LLM API concepts stage by stage using the Groq SDK.

## Done Stages
- Stage 1: Basic call - src/stage1_basic.py, src/common.py

## Current Stage
Stage 1: Basic call - send one message, print reply and token usage.
Status: DONE. Next: Stage 2 - Conversation memory.

## Key Decisions
- Model: qwen/qwen3.8-27b (configurable via GROQ_MODEL env var)
- Language: Python 3.11+, official groq SDK only
- API key: Read from GROQ_API_KEY environment variable
- Each stage in its own file under src/
- Shared helpers in src/common.py
- Files under 120 lines

## Known Problems or Open Questions
- None

## How to Run and Test
```bash
cd /home/shivu/Downloads/llm-api-lab
source venv/bin/activate
python src/stage1_basic.py
```