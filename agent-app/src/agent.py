from langchain.agents import create_agent
from middleware.error import handle_tool_errors
from tools.sample import send_email
from mcp.atlassian import mcp_client


mcp_tools = mcp_client.get_tools()
agent = create_agent(
    "openai:gpt-4o",
    tools=[send_email, *mcp_tools],
    middleware=[handle_tool_errors],
    system_prompt="You are an email assistant. Always use the send_email tool.",
)
    

