## MCP Birdwatching

This repository contains a complete stack for working with the Model Context Protocol (MCP), which allows AI (Claude) to interact with birdwatching data. The project includes an MCP server, a client part on FastAPI, and automation tools for deployment.

### Project structure

The project is divided into several main modules:

- birdwatching_mcp_server/: The server part of MCP. Connects to the external Birdwatching API and provides the get_gallery tool.

- birdwatching_mcp_client/: The client part on FastAPI. A server that allows the user to ask Claude questions using the capabilities of the MCP server.

- ansible/: Configuration files (playbooks and roles) for automatic server and client setup on EC2 instances.

- jenkins/jenkinsfile.mcp: Pipeline for automating CI/CD processes (granting AWS permissions, running Ansible).

### Components

Detailed instructions for each module can be found in the corresponding folders:

1. MCP Server

```
birdwatching_mcp_server/README.md
```

2. MCP Client

```
birdwatching_mcp_client/README.md
```

### Automation (Ansible & Jenkins)

`inventory.ini` must contain a host group with the specified name `[mcp]`
For example

```
[mcp]
host1
```

To run the pipeline for instance configuration, add the following variables to Jenkins credentials:

```
client_port=""
anthropic_api_key=""
app_user=""
gallery_url=""
```

Build the job
