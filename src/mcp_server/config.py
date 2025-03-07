"""
Configuration module for the GitHub MCP Server
"""
import os
from typing import List, Optional

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Server configuration settings."""

    # GitHub API Configuration
    github_api_token: str = Field(..., env="GITHUB_API_TOKEN")
    github_api_base_url: str = Field("https://api.github.com", env="GITHUB_API_BASE_URL")

    # MCP Server Configuration
    mcp_server_host: str = Field("0.0.0.0", env="MCP_SERVER_HOST")
    mcp_server_port: int = Field(8000, env="MCP_SERVER_PORT")
    mcp_server_debug: bool = Field(False, env="MCP_SERVER_DEBUG")
    mcp_server_log_level: str = Field("info", env="MCP_SERVER_LOG_LEVEL")

    # Authentication
    mcp_api_key: Optional[str] = Field(None, env="MCP_API_KEY")

    # Caching Configuration
    cache_enabled: bool = Field(True, env="CACHE_ENABLED")
    cache_ttl: int = Field(3600, env="CACHE_TTL")  # Time to live in seconds

    # Rate Limiting
    rate_limit_enabled: bool = Field(True, env="RATE_LIMIT_ENABLED")
    rate_limit_max_calls: int = Field(5000, env="RATE_LIMIT_MAX_CALLS")

    # CORS
    cors_origins: List[str] = Field(["*"], env="CORS_ORIGINS")

    class Config:
        """Pydantic config."""

        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Create settings instance
settings = Settings() 