# Project DT

Local Atlassian (Jira + Confluence) stack with an agent app that integrates via LangGraph/tools.

- Atlassian stack: [atlassian/docker-compose.yml](./atlassian/docker-compose.yml), [atlassian/nginx.conf](./atlassian/nginx.conf)
- Example REST calls: [example.http](./example.http)
- Agent app entrypoint: [agent-app/main.py](./agent-app/main.py)
- Python project files: [agent-app/pyproject.toml](./agent-app/pyproject.toml), [agent-app/requirement.txt](./agent-app/requirement.txt)

## Prerequisites

- Docker Desktop (or Docker + Docker Compose v2)
- Python 3.11+ (see [.python-version](./agent-app/.python-version) if present)
- VS Code (recommended) with “REST Client” extension for using [example.http](./example.http)

## Quick start

1. Start Jira and Confluence locally

```sh
cd atlassian
docker compose up -d
```

2. Add hosts entries

- macOS/Linux: `sudo sh -c 'echo "127.0.0.1 jira.localhost confluence.localhost" >> /etc/hosts'`
- Windows (Admin): add the same line to C:\Windows\System32\drivers\etc\hosts

3. Finish first-time setup in browser

- Jira: http://jira.localhost
- Confluence: http://confluence.localhost

Create an admin user and complete the onboarding wizards.

4. Create Personal Access Tokens (PAT)

- In Jira and Confluence, generate PATs for your admin user.
- Put them in the root `.env` for using [example.http](./example.http):

```ini
# .env (repo root)
PAT_CONFLUENCE=your_confluence_pat
PAT_JIRA=your_jira_pat
```

5. Configure the agent app

Create/update [agent-app/.env](./agent-app/.env):

```ini
CONFLUENCE_BASE_URL=http://confluence.localhost
JIRA_BASE_URL=http://jira.localhost
CONFLUENCE_PAT=your_confluence_pat
JIRA_PAT=your_jira_pat
```

6. Install and run the agent app

```sh
# from repo root
python -m venv .venv
# Windows: .\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Prefer pyproject if available, else fallback to requirements
pip install -e ./agent-app || pip install -r ./agent-app/requirement.txt

python ./agent-app/main.py
```

## Using the REST examples

Open [example.http](./example.http) in VS Code and click “Send Request” on any block.  
It uses the tokens from the root [.env](./.env).

- Create page in Confluence: first POST block.
- Search your pages: GET /rest/api/content/search
- Jira JQL autocomplete: GET /rest/api/3/jql/autocompletedata

## Project structure

```
.
├── atlassian/                # Docker Compose for Jira + Confluence + NGINX
│   ├── docker-compose.yml    # Docker Compose file
│   └── nginx.conf            # NGINX configuration
├── agent-app/                # LangChain agent app
│   ├── main.py                # Entry point
│   ├── src/                   # Source code
│   │   ├── loader/            # Loaders for different data sources
│   │   │   ├── atlassian.py   # Atlassian loader
│   │   └── ...                # Other source files
│   ├── .env                   # Environment variables
│   ├── pyproject.toml         # Python project configuration
│   └── requirement.txt        # Python dependencies
└── example.http              # HTTP request examples
```
