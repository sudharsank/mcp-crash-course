from typing import List

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    return "It's raining in Singapore"


if __name__ == "__main__":
    mcp.run(transport="sse")
