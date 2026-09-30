import json
import os
import time
from common import get_client, MODEL, print_usage

MAX_ITERATIONS = 8
MAX_RETRIES = 3

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a file from the workspace",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Relative path from workspace/"}
                },
                "required": ["path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "List files in the workspace",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "Relative path from workspace/", "default": "."}
                },
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluate a math expression",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "Math expression like '2 + 3 * 4'"}
                },
                "required": ["expression"]
            }
        }
    }
]

def read_file(path: str) -> str:
    full = os.path.join("workspace", path)
    if not os.path.exists(full):
        return f"Error: File not found: {path}"
    with open(full, "r") as f:
        return f.read()

def list_files(path: str = ".") -> str:
    full = os.path.join("workspace", path)
    if not os.path.exists(full):
        return f"Error: Path not found: {path}"
    files = os.listdir(full)
    return "\n".join(files) if files else "(empty)"

def calculate(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {e}"

def call_tool(name: str, args: dict) -> str:
    if name == "read_file":
        return read_file(args["path"])
    elif name == "list_files":
        return list_files(args.get("path", "."))
    elif name == "calculate":
        return calculate(args["expression"])
    return f"Error: Unknown tool {name}"

def run_with_retry(client, messages, tools):
    for attempt in range(MAX_RETRIES):
        try:
            return client.chat.completions.create(
                model=MODEL,
                max_completion_tokens=500,
                messages=messages,
                tools=tools
            )
        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                raise
            wait = 2 ** attempt
            print(f"Error: {e}. Retrying in {wait}s...")
            time.sleep(wait)

def main() -> None:
    client = get_client()

    messages = [
        {"role": "system", "content": "You have access to tools. Use them to answer the user's question."},
        {"role": "user", "content": "List the files in workspace, then read any .txt file you find, then calculate 15 * 7 + 3"}
    ]

    for iteration in range(MAX_ITERATIONS):
        print(f"\n--- Iteration {iteration + 1} ---")
        response = run_with_retry(client, messages, TOOLS)

        msg = response.choices[0].message
        finish_reason = response.choices[0].finish_reason

        if finish_reason != "tool_calls":
            print(f"Final: {msg.content}")
            print_usage(response.usage)
            break

        messages.append({"role": "assistant", "content": msg.content, "tool_calls": [
            {"id": tc.id, "type": "function", "function": {"name": tc.function.name, "arguments": tc.function.arguments}}
            for tc in msg.tool_calls
        ]})

        for tc in msg.tool_calls:
            args = json.loads(tc.function.arguments)
            print(f"Tool: {tc.function.name}({args})")
            result = call_tool(tc.function.name, args)
            print(f"Result: {result[:200]}...")
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": result
            })
    else:
        print("Max iterations reached")

if __name__ == "__main__":
    main()