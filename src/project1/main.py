import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()


@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmatic calculations with numbers"""
    print("Tool has been called.")
    return f"The sum of {a} and {b} is {a+b}"


def main():
    model = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        temperature=0
    )

    tools = [calculator]
    agent_executor = create_agent(model, tools)

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou:  ").strip()

        if user_input == "quit":
            break

        print("\nAssistant: ", end="")

        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "model" in chunk:
                for message in chunk["model"]["messages"]:

                    if isinstance(message.content, list):
                        for item in message.content:
                            if isinstance(item, dict) and "text" in item:
                                print(item["text"], end="")
                    else:
                        print(message.content, end="")

        print()


if __name__ == "__main__":
    main()