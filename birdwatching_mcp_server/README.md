# MCP Birdwatching Server

MCP Birdwatching Server is a server for MCP that connects to the Birdwatching Flask application and provides a tool for obtaining a gallery of photos of birds and their locations.

## Features

- Connecting to the Birdwatching Flask application via REST API
- MCP tool get_gallery for obtaining a list of photos and locations)

## Requirements

```
httpx>=0.28.1
mcp[cli]>=1.22.0
requests>=2.32.5
```

## Setting up

1. Clone this repo:

```
git clone https://github.com/Core5-team/birdwatching_mcp.git"
```

2. Go to:

```
cd birdwatching_mcp_server
```

3. Setting Up Your Environment

```
# Create virtual environment
uv venv

# Activate virtual environment
.venv\Scripts\activate

# Install required packages
uv add mcp[cli] httpx requests
```

4. Create an .env file:

```
GALLERY_URL={{ gallery_url}}
```

GALLERY_URL — URL of the gallery in the Birdwatching Flask application

5. Run:

```
python main.py
```
