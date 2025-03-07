# API Documentation

## Overview

The GitHub MCP Server provides a Model Context Protocol (MCP) interface for GitHub repositories. This document describes the API endpoints and their usage.

## Base URL

The base URL for all API endpoints is:

```
https://your-mcp-server.herokuapp.com
```

For local development:

```
http://localhost:8000
```

## Authentication

All MCP endpoints require authentication using an API key. The API key should be provided in the `Authorization` header:

```
Authorization: Bearer your_api_key
```

## Endpoints

### Health Check

```
GET /health
```

Returns the health status of the server.

**Response:**

```json
{
  "status": "healthy"
}
```

### Root

```
GET /
```

Returns basic information about the server.

**Response:**

```json
{
  "name": "GitHub MCP Server",
  "version": "0.1.0",
  "description": "A Model Context Protocol server for GitHub repositories"
}
```

### MCP Endpoints

The MCP endpoints will be implemented according to the [Model Context Protocol specification](https://github.com/modelcontextprotocol/mcp). These endpoints will be documented in detail as they are implemented.

## Error Handling

All API errors return a JSON response with a `detail` field describing the error:

```json
{
  "detail": "Error message"
}
```

HTTP status codes are used to indicate the type of error:

- `400 Bad Request`: Invalid request parameters
- `401 Unauthorized`: Missing or invalid API key
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Resource not found
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Server error

## Rate Limiting

The server implements rate limiting to prevent abuse and to stay within GitHub API rate limits. Rate limit information is provided in the response headers:

- `X-RateLimit-Limit`: Maximum number of requests allowed per hour
- `X-RateLimit-Remaining`: Number of requests remaining in the current rate limit window
- `X-RateLimit-Reset`: Time at which the rate limit window resets (Unix timestamp) 