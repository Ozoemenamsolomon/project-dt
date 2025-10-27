import os
from langchain_mcp_adapters.client import MultiServerMCPClient 

confluence_url = os.getenv("CONFLUENCE_URL", "")
confluence_token = os.getenv("CONFLUENCE_PERSONAL_TOKEN", "")
jira_url = os.getenv("JIRA_URL", "")
jira_token = os.getenv("JIRA_PERSONAL_TOKEN", "")

mcp_client = MultiServerMCPClient(  
    {
        # TODO: remove this example weather tool config when not needed
        "weather": {
            "transport": "streamable_http",  # HTTP-based remote server
            # Ensure you start your weather server on port 8000
            "url": "http://localhost:8000/mcp",
        },
        "mcp-atlassian": {
            "transport": "stdio",
            "command": "docker",
            "env": {
                "CONFLUENCE_URL": confluence_url,
                "CONFLUENCE_PERSONAL_TOKEN": confluence_token,
                "CONFLUENCE_SSL_VERIFY": "false",
                "JIRA_URL": jira_url,
                "JIRA_PERSONAL_TOKEN": jira_token,
                "JIRA_SSL_VERIFY": "false"
            },
            "args": [
                "run",
                "--rm",
                "-i",
                "-e", "CONFLUENCE_URL",
                "-e", "CONFLUENCE_PERSONAL_TOKEN",
                "-e", "CONFLUENCE_SSL_VERIFY",
                "-e", "JIRA_URL",
                "-e", "JIRA_PERSONAL_TOKEN",
                "-e", "JIRA_SSL_VERIFY",
                "ghcr.io/sooperset/mcp-atlassian:latest"
            ]
        },
    }
)

