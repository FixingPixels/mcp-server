# Environment Setup Guide

This document provides instructions for setting up the development environment for the GitHub MCP server project.

## Prerequisites

- Python 3.11+ (required for MCP SDK compatibility)
- Git
- GitHub account
- Heroku account (for deployment)

## Setup Steps

### 1. Clone the Repository

```bash
git clone https://github.com/FixingPixels/mcp-server.git
cd mcp-server
```

### 2. Create a Virtual Environment

```bash
# Create a virtual environment with Python 3.11+
python3.11 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Update pip, setuptools, and wheel
pip install -U pip setuptools wheel

# Install dependencies from requirements.txt
pip install -r requirements.txt
```

> **Note**: The MCP SDK requires Python 3.10 or higher. If you encounter issues with the installation, make sure you're using a compatible Python version.

### 4. Set Up Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file with your GitHub API token and other settings
```

### 5. Set Up Pre-commit Hooks

```bash
# Install pre-commit hooks
pre-commit install
```

### 6. Verify the Setup

```bash
# Run tests to verify the setup
python -m pytest
```

## Development Tools

The project uses the following development tools:

- **pytest**: For testing
- **black**: For code formatting
- **flake8**: For linting
- **isort**: For import sorting
- **pre-commit**: For running checks before commits

## Troubleshooting

### MCP SDK Installation Issues

If you encounter issues installing the MCP SDK, try installing it directly from GitHub:

```bash
pip install git+https://github.com/modelcontextprotocol/python-sdk.git
```

### Python Version Compatibility

The MCP SDK requires Python 3.10 or higher. If you're using an older version, you'll need to upgrade:

```bash
# Check your Python version
python --version

# Install a newer version if needed (using your package manager)
```

### Pre-commit Hook Issues

If pre-commit hooks are failing, you can run them manually to see the issues:

```bash
pre-commit run --all-files
```
