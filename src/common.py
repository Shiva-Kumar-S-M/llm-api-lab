import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def get_client() -> Groq:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not set. Copy .env.example to .env and add your key.")
    return Groq(api_key=api_key)

MODEL = os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b")

def print_usage(usage) -> None:
    print(f"\nTokens: input={usage.prompt_tokens} output={usage.completion_tokens} total={usage.total_tokens}")