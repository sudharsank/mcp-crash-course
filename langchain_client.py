import asyncio

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-2025-04-14")


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    "/Users/sudharsank/Documents/Workouts/MCP/mcp-crash-course/servers/math_server.py"
                ],
                "transport": "stdio",
            },
            "weather": {"url": "http://127.0.0.1:8000/sse", "transport": "sse"},
        }
    )
    tools = await client.get_tools()
    agent = create_react_agent(llm, tools)
    result = await agent.ainvoke(
        {
            "messages": [
                HumanMessage(content="What is 54 + 2 * 3? Use the tools to solve."),
                HumanMessage(content="What is the weather in Singapore?"),
            ]
        }
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
