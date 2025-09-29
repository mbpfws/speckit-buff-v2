"""
Context7 MCP Server Integration

Provides library documentation and code examples through Context7 MCP server
for enhanced AI coding workflows across all 10 supported platforms.
"""
from typing import Dict, Any, Optional, List
from ..mcp import MCPServerType, MCPServerConfig, MCPIntegrationManager


class Context7Integration:
    """
    Integration with Context7 MCP server for library documentation and code examples
    """
    
    def __init__(self, mcp_manager: MCPIntegrationManager):
        self.mcp_manager = mcp_manager
        self.server_type = MCPServerType.CONTEXT7
        
    def resolve_library_id(self, library_name: str) -> Dict[str, Any]:
        """Resolve library name to Context7-compatible library ID"""
        try:
            result = self.mcp_manager.execute_tool(
                self.server_type,
                "resolve-library-id",
                {"libraryName": library_name}
            )
            return result
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to resolve library ID: {e}",
                "server": self.server_type.value
            }
    
    def get_library_docs(
        self, 
        library_id: str, 
        topic: str = "", 
        tokens: int = 5000
    ) -> Dict[str, Any]:
        """Get documentation for a specific library"""
        try:
            result = self.mcp_manager.execute_tool(
                self.server_type,
                "get-library-docs",
                {
                    "context7CompatibleLibraryID": library_id,
                    "topic": topic,
                    "tokens": tokens
                }
            )
            return result
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to get library docs: {e}",
                "server": self.server_type.value
            }
    
    def search_library_documentation(
        self, 
        library_name: str, 
        topic: str = ""
    ) -> Dict[str, Any]:
        """Convenience method to search and get documentation in one call"""
        # First resolve library ID
        resolve_result = self.resolve_library_id(library_name)
        
        if not resolve_result.get("success", False):
            return resolve_result
            
        # Extract library ID from result
        library_info = resolve_result.get("result", {})
        if "library_id" not in library_info:
            return {
                "success": False,
                "error": "Could not extract library ID from resolve result",
                "server": self.server_type.value
            }
            
        # Get documentation
        return self.get_library_docs(library_info["library_id"], topic)
    
    def get_python_library_docs(self, library_name: str, topic: str = "") -> Dict[str, Any]:
        """Get documentation for Python libraries"""
        return self.search_library_documentation(library_name, topic)
    
    def get_javascript_library_docs(self, library_name: str, topic: str = "") -> Dict[str, Any]:
        """Get documentation for JavaScript libraries"""
        return self.search_library_documentation(library_name, topic)
    
    def get_framework_docs(self, framework_name: str, topic: str = "") -> Dict[str, Any]:
        """Get documentation for frameworks"""
        return self.search_library_documentation(framework_name, topic)


def create_context7_integration() -> Context7Integration:
    """Factory function to create Context7 integration"""
    mcp_manager = MCPIntegrationManager()
    
    # Register Context7 configuration
    context7_config = MCPServerConfig(
        server_type=MCPServerType.CONTEXT7,
        endpoint="npx -y @upstash/context7-mcp@latest",
        timeout=30
    )
    mcp_manager.register_server(context7_config)
    
    # Connect to server
    mcp_manager.connect_server(MCPServerType.CONTEXT7)
    
    return Context7Integration(mcp_manager)