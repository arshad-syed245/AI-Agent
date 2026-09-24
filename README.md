# AI Agent (project1)

A simple command-line AI agent built with Python, LangChain, and LangGraph. The agent chats with the user and can call a calculator tool.

## Features

- Chat with an AI assistant in the terminal
- Tool calling: the agent can use a `calculator` tool
- Streaming responses
- API key loaded safely from a `.env` file

## Tech Stack

- Python 3.13
- [uv](https://github.com/astral-sh/uv) for package and environment management
- LangChain (`langchain`, `langchain-core`)
- LangGraph
- `langchain-google-genai` (Google Gemini)
- `python-dotenv`

## Project Structure

```
project1/
├── src/project1/
│   ├── __init__.py
│   └── main.py
├── pyproject.toml
├── uv.lock
└── .env          (not committed)
```

## Setup

1. Install dependencies:
```
   uv sync
```
2. Create a `.env` file in the project folder:
```
   GOOGLE_API_KEY=your_api_key_here
```
3. Run the agent:
```
   uv run python .\src\project1\main.py
```

Type `quit` to exit.

## Current Status: Blocked

The code runs and starts correctly, but the project is currently **not working** because of an account problem on Google's side, not a bug in the code.

When sending any message, the Gemini API returns:

```
403 PERMISSION_DENIED: Your project has been denied access. Please contact support.
```

What I tried:

- Fixed the file path and the deprecated `create_react_agent` import
- Confirmed no old key was set in the Windows environment variables
- Created a new API key in a new project, with the same error

Because a new key gives the same error, the block appears to be on my Google account or project, not on the key. Google says support must resolve it.

## Known Issues / Limitations

- **Google account block:** the Gemini API is unavailable until Google resolves it.
- **Calculator tool only adds:** the `calculator` function returns `a + b`, even though its description says "basic arithmetic". It should be extended to support subtraction, multiplication, and division.
- Model name (`gemini-3.1-flash-lite`) should be verified against what the API supports.

## Next Steps

- Contact Google support or appeal the block, or try a different Google account
- Or switch to another model provider by changing only the model line and import
- Improve the calculator tool to support all basic operations
- Add error handling around API calls so failures show a clear message instead of a long traceback