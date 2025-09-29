"""
Tavily Expert MCP Server Integration

Provides web search and content extraction capabilities through Tavily Expert MCP server
for enhanced AI coding workflows across all 10 supported platforms.
"""
from typing import Dict, Any, Optional, List
import json
from ..mcp import MCPServerType, MCPServerConfig, MCPIntegrationManager


class TavilyExpertIntegration:
    """
    Integration with Tavily Expert MCP server for web search and content extraction
    """
    
    def __init__(self, mcp_manager: MCPIntegrationManager):
        self.mcp_manager = mcp_manager
        self.server_type = MCPServerType.TAVILY_EXPERT
        
    def start_tavily_expert(self, intent: str) -> Dict[str, Any]:
        """Start Tavily Expert with specific intent"""
        try:
            result = self.mcp_manager.execute_tool(
                self.server_type,
                "tavily_start_tool",
                {"what_is_your_intent": intent}
            )
            return result
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to start Tavily Expert: {e}",
                "server": self.server_type.value
            }
    
    def search_web(self, query: str, search_depth: str = "basic", max_results: int = 10) -> Dict[str, Any]:
        """Perform web search using Tavily Expert"""
        try:
            result = self.mcp_manager.execute_tool(
                self.server_type,
                "tavily_search_tool",
                {
                    "what_is_your_intent": f"Search for information about {query}",
                    "query": query,
                    "search_depth": search_depth,
                    "max_results": max_results,
                    "include_answer": True,
                    "include_raw_content": False
                }
            )
            return result
        except Exception as e:
            return {
                "success": False,
                "error": f"Web search failed: {e}",
                "server": self.server_type.value
            }
    
    def extract_content(self, urls: List[str], include_images: bool = False) -> Dict[str, Any]:
        """Extract content from URLs using Tavily Expert"""
        try:
            result = self.mcp_manager.execute_tool(
                self.server_type,
                "tavily_extract_tool",
                {
                    "what_is_your_intent": "Extract content from provided URLs",
                    "urls": urls,
                    "include_images": include_images,
                    "extract_depth": "basic"
                }
            )
            return result
        except Exception as e:
            return {
                "success": False,
                "error": f"Content extraction failed: {e}",
                "server": self.server_type.value
            }
    
    def get_api_docs(self) -> Dict[str, Any]:
        """Get Tavily API documentation"""
        try:
            result = self.mcp_manager.execute_tool(
                self.server_type,
                "tavily_get_api_docs_tool",
                {}
            )
            return result
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to get API docs: {e}",
                "server": self.server_type.value
            }
    
    def get_best_practices(self) -> Dict[str, Any]:
        """Get Tavily best practices"""
        try:
            result = self.mcp_manager.execute_tool(
                self.server_type,
                "tavily_get_search_best_practices_tool",
                {}
            )
            return result
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to get best practices: {e}",
                "server": self.server_type.value
            }


def create_tavily_expert_integration() -> TavilyExpertIntegration:
    """Factory function to create Tavily Expert integration"""
    mcp_manager = MCPIntegrationManager()
    
    # Register Tavily Expert configuration
    tavily_config = MCPServerConfig(
        server_type=MCPServerType.TAVILY_EXPERT,
        endpoint="npx -y @modelcontextprotocol/server-tavily-expert",
        timeout=60
    )
    mcp_manager.register_server(tavily_config)
    
    # Connect to server
    mcp_manager.connect_server(MCPServerType.TAVILY_EXPERT)
    
    return TavilyExpertIntegration(mcp_manager)