# MCP Birdwatching Client

This is a server based on FastAPI that allows to communicate with Claude (Anthropic) via the Model Context Protocol.
The server automatically connects to your MCP server, obtains the available tools, and allows to make requests to Claude with tool use support.

## Features

- Single `POST /query` endpoint
- Automatic discovery and use of all tools from MCP server
- Full conversation history saved as JSON (`conversations/`)

## Requirements

```
fastapi>=0.123.0
mcp>=1.22.0
anthropic>=0.75.0
python-dotenv>=1.2.1
uvicorn>=0.22.0
```

## Setting up

1. Clone this repo:

```
git clone https://github.com/Core5-team/birdwatching_mcp.git"
```

2. Go to:

```
cd birdwatching_mcp_client
```

3. Setting Up Your Environment

```
# Create virtual environment
uv venv

# Activate virtual environment
.venv\Scripts\activate

# Install required packages
uv add mcp anthropic python-dotenv
```

4. Create an .env file:

```
server_script_path={{ path_to_server }}
ANTHROPIC_API_KEY={{ anthropic_api_key }}
port={{ port_mcp_client }}
```

server_script_path — path to the MCP server (.py or .js)
ANTHROPIC_API_KEY — Anthropic key for Claude
port — port on which FastAPI will run

5. Run:

```
uvicorn main:app --reload
```
