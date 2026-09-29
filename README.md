# AI Agent (project1)

A simple command-line AI agent built with Python, LangChain, and Google Gemini.

The agent can chat with the user and can decide when to use a calculator tool to perform calculations.

## Features

* Chat with an AI assistant in the terminal
* Tool calling using a calculator tool
* The AI agent can decide when to use the calculator
* Streaming responses
* Google Gemini as the AI model
* API key loaded safely from a `.env` file
* Simple command-line interface

## Tech Stack

* Python 3.13
* [uv](https://github.com/astral-sh/uv) for package and environment management
* LangChain
* LangChain Core
* LangGraph
* `langchain-google-genai` for Google Gemini
* `python-dotenv`

## How the Project Works

The project uses an AI agent that receives the user's message and decides how to respond.

For example, if the user asks:

```text
7 + 7?
```

The agent can decide to call the `calculator` tool.

The calculator performs the calculation and returns:

```text
The sum of 7 and 7 is 14
```

The agent then gives the final answer to the user.

For normal messages such as:

```text
Hi
```

the agent can simply respond using the Gemini model without using the calculator.

## Project Structure

```text
project1/
│
├── src/
│   └── project1/
│       ├── __init__.py
│       └── main.py
│
├── pyproject.toml
├── uv.lock
├── .gitignore
└── .env
```

The `.env` file contains the API key and should **not** be uploaded to GitHub.

## Setup

### 1. Install Dependencies

Make sure `uv` is installed.

Then, from the project folder, run:

```powershell
uv sync
```

This installs the required packages and sets up the project environment.

### 2. Create the `.env` File

Create a file named:

```text
.env
```

in the main project folder:

```text
project1/
├── .env
├── pyproject.toml
└── src/
```

Add your Google API key:

```text
GOOGLE_API_KEY=your_api_key_here
```

Do not share your API key publicly.

The project uses `python-dotenv` to load the API key from the `.env` file.

### 3. Run the Agent

Open PowerShell and go to the project folder:

```powershell
cd "D:\AI agent\project1"
```

Then run:

```powershell
uv run python src\project1\main.py
```

The program should start with:

```text
Welcome! I'm your AI assistant. Type 'quit' to exit.
You can ask me to perform calculations or chat with me.
```

## Example

### Normal Conversation

```text
You: hi

Assistant: Hello! How can I help you today?
```

### Calculator Tool

```text
You: 7+7?

Assistant: 7 + 7 = 14
```

The agent decides that the calculator tool is useful for this question and calls it automatically.

## Calculator Tool

The project currently contains a simple calculator tool:

```python
@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmatic calculations with numbers"""
    return f"The sum of {a} and {b} is {a+b}"
```

At the moment, the calculator performs addition.

For example:

```text
7 + 7
```

returns:

```text
The sum of 7 and 7 is 14
```

The calculator can be extended later to support subtraction, multiplication, and division.

## Model

The project currently uses Google Gemini through:

```python
ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0
)
```

The previous version of this project used a different setup and had problems with the API access.

The project has now been updated to use **Google Gemini** and the newer LangChain agent creation method:

```python
from langchain.agents import create_agent
```

instead of the previously used:

```python
from langgraph.prebuilt import create_react_agent
```

This change was made because the older agent creation method was deprecated in the newer LangChain setup.

## Current Status

**Working**

The current version of the project:

* Starts successfully
* Connects to Google Gemini
* Accepts user messages
* Can respond to normal conversations
* Can call the calculator tool
* Can return calculation results
* Uses the `.env` file for the Google API key

Example:

```text
You: 7+7?

Assistant: 7 + 7 = 14
```

## Warning About the Model

Depending on the installed version of `langchain-google-genai`, Gemini may show a warning related to the `temperature` parameter:

```text
UserWarning: Model 'gemini-3.5-flash-lite' uses fixed sampling defaults;
the sampling parameter(s) temperature will be ignored.
```

This is a warning, not a program error.

The current code hides this warning so that the terminal shows the normal assistant response instead of unnecessary warning information.

## Security

The Google API key is stored in:

```text
.env
```

The `.env` file should **never be committed to GitHub**.

The `.gitignore` file should contain:

```text
.env
```

This prevents the API key from accidentally being uploaded to the repository.

## Future Improvements

Possible improvements for this project include:

* Add subtraction, multiplication, and division to the calculator
* Add more useful tools
* Add error handling
* Add a web search tool
* Add a weather tool
* Add memory so the agent can remember previous messages
* Create a graphical user interface
* Add multiple AI models and compare their responses
* Add logging to study how the agent decides which tool to use
* Study whether the AI agent behaves differently depending on how a question is written

## Relevance to My AI and LLM Learning

This project helped me understand the basic concepts of:

* Large Language Models (LLMs)
* AI agents
* Tool calling
* LangChain
* LangGraph
* Google Gemini
* Environment variables
* API keys
* Streaming responses

It also provides a foundation for future projects involving **LLM evaluation and LLM bias research**.

## License

This project is created for learning and educational purposes.
