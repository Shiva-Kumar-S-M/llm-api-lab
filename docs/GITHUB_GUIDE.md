# GitHub Guide

## Final Folder Structure

```
llm-api-lab/
├── src/
│   ├── common.py
│   ├── stage1_basic.py
│   ├── stage2_conversation.py
│   ├── stage3_streaming.py
│   ├── stage4_structured.py
│   └── stage5_tools.py
├── workspace/
├── docs/
│   ├── STATE.md
│   ├── HOW_IT_WORKS.md
│   ├── PROMPT_NOTES.md
│   └── GITHUB_GUIDE.md
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## .gitignore Content

```
.env
__pycache__/
venv/
*.pyc
*.pyo
*.pyd
.Python
.pytest_cache/
.coverage
htmlcov/
*.egg-info/
dist/
build/
```

## Recommended First Commit Message

```
Initial commit: project structure, stage 1 basic call
```

## Suggested Commit Message Per Stage

- Stage 1: `Stage 1: Basic call with Groq API`
- Stage 2: `Stage 2: Conversation memory and token tracking`
- Stage 3: `Stage 3: Streaming response`
- Stage 4: `Stage 4: Structured JSON output with validation`
- Stage 5: `Stage 5: Tool use loop with read_file, list_files, calculate`

## Suggested Branch Name

```
main
```

Or for feature branches:
```
stage-1-basic
stage-2-conversation
stage-3-streaming
stage-4-structured
stage-5-tools
```

## Commands to Run Yourself Later

```bash
# Initialize git (run once)
git init

# Add all files
git add .

# First commit
git commit -m "Initial commit: project structure, stage 1 basic call"

# Add remote (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/llm-api-lab.git

# Push to GitHub
git push -u origin main
```

## Checklist

- [ ] No API key in any file (check .env is ignored)
- [ ] .env is in .gitignore
- [ ] README.md is up to date
- [ ] STATE.md is current
- [ ] All stage files exist under src/
- [ ] requirements.txt has groq and python-dotenv