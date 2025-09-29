"""
Fetch MCP Server Integration

Provides web content fetching capabilities through Fetch MCP server
for enhanced AI coding workflows across all 10 supported platforms.
"""
from typing import Dict, Any, Optional
from ..mcp import MCPServerType, MCPServerConfig, MCPIntegrationManager


class FetchIntegration:
    """
    Integration with Fetch MCP server for web content fetching
    """
    
    def __init__(self, mcp_manager: MCPIntegrationManager):
        self.mcp_manager = mcp_manager
        self.server_type = MCPServerType.FETCH
        
    def fetch_url(self, url: str, max_length: int = 5000, raw: bool = False) -> Dict[str, Any]:
        """Fetch content from a URL"""
        try:
            result = self.mcp_manager.execute_tool(
                self.server_type,
                "fetch",
                {
                    "url": url,
                    "max_length": max_length,
                    "raw": raw
                }
            )
            return result
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to fetch URL: {e}",
                "server": self.server_type.value
            }
    
    def fetch_multiple_urls(self, urls: list, max_length: int = 5000) -> Dict[str, Any]:
        """Fetch content from multiple URLs"""
        results = {}
        for url in urls:
            result = self.fetch_url(url, max_length)
            results[url] = result
            
        return {
            "success": True,
            "results": results,
            "total_urls": len(urls),
            "successful_fetches": sum(1 for r in results.values() if r.get("success", False))
        }
    
    def fetch_github_repo_info(self, owner: str, repo: str) -> Dict[str, Any]:
        """Fetch GitHub repository information"""
        urls = [
            f"https://api.github.com/repos/{owner}/{repo}",
            f"https://github.com/{owner}/{repo}",
            f"https://raw.githubusercontent.com/{owner}/{repo}/main/README.md"
        ]
        
        return self.fetch_multiple_urls(urls)
    
    def fetch_documentation(self, base_url: str, endpoints: list) -> Dict[str, Any]:
        """Fetch documentation from multiple endpoints"""
        urls = [f"{base_url}{endpoint}" for endpoint in endpoints]
        return self.fetch_multiple_urls(urls)


def create_fetch_integration() -> FetchIntegration:
    """Factory function to create Fetch integration"""
    mcp_manager = MCPIntegrationManager()
    
    # Register Fetch configuration
    fetch_config = MCPServerConfig(
        server_type=MCPServerType.FETCH,
        endpoint="uvx mcp-server-fetch",
        timeout=30
    )
    mcp_manager.register_server(fetch_config)
    
    # Connect to server
    mcp_manager.connect_server(MCPServerType.FETCH)
    
    return FetchIntegration(mcp_manager)