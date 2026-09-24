from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
#from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmatic calculations with numbers"""
    print("Tool has been called. ")
    return f"The sum of {a} and {b} is {a+b}"

def main():
    model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)

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
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()