# GitHub MCP Server

A Model Context Protocol (MCP) server for GitHub repositories, built using the Python SDK.

## Overview

This server implements the [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/mcp) for GitHub repositories, allowing AI assistants to access repository context such as files, commits, issues, and pull requests. It's built using the [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) and designed to be deployed on Heroku.

## Features

- Access GitHub repository files and content
- Retrieve commit history
- Access issues and pull requests
- Secure authentication and access control
- Rate limiting and caching for GitHub API
- Compatible with MCP-enabled AI assistants

## Requirements

- Python 3.8+
- GitHub API access
- Heroku account (for deployment)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/FixingPixels/mcp-server.git
   cd mcp-server
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```
   cp .env.example .env
   # Edit .env with your GitHub API token and other settings
   ```

## Usage

### Local Development

```
uvicorn src.mcp_server.main:app --reload
```

### Deployment

This server is designed to be deployed on Heroku. See the [deployment documentation](docs/deployment.md) for details.

## Documentation

- [API Documentation](docs/api.md)
- [Configuration Guide](docs/configuration.md)
- [Deployment Guide](docs/deployment.md)
- [Troubleshooting](docs/troubleshooting.md)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 