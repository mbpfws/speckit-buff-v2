"""
MCP Server Orchestrator

Coordinates all MCP server integrations and provides unified interface
for enhanced AI coding workflows across all 10 supported platforms.
"""
from typing import Dict, Any, Optional
from .tavily_integration import create_tavily_integration
from .context7_integration import create_context7_integration
from .deepwiki_integration import create_deepwiki_integration
from .fetch_integration import create_fetch_integration
from .mcp import MCPServerType, MCPServerStatus


class MCPOrchestrator:
    """
    Orchestrates all MCP server integrations for enhanced AI coding workflows
    """
    
    def __init__(self):
        self.integrations = {}
        self.server_status = {}
        
    def initialize_all_integrations(self) -> Dict[str, Any]:
        """Initialize all MCP server integrations"""
        try:
            # Initialize Tavily Expert integration
            tavily_integration = create_tavily_integration()
            self.integrations[MCPServerType.TAVILY_EXPERT] = tavily_integration
            self.server_status[MCPServerType.TAVILY_EXPERT] = MCPServerStatus.CONNECTED
            
            # Initialize Context7 integration
            context7_integration = create_context7_integration()
            self.integrations[MCPServerType.CONTEXT7] = context7_integration
            self.server_status[MCPServerType.CONTEXT7] = MCPServerStatus.CONNECTED
            
            # Initialize DeepWiki integration
            deepwiki_integration = create_deepwiki_integration()
            self.integrations[MCPServerType.DEEPWIKI] = deepwiki_integration
            self.server_status[MCPServerType.DEEPWIKI] = MCPServerStatus.CONNECTED
            
            # Initialize Fetch integration
            fetch_integration = create_fetch_integration()
            self.integrations[MCPServerType.FETCH] = fetch_integration
            self.server_status[MCPServerType.FETCH] = MCPServerStatus.CONNECTED
            
            return {
                "success": True,
                "initialized_servers": len(self.integrations),
                "server_status": {k.value: v.value for k, v in self.server_status.items()},
                "available_servers": [server.value for server in self.integrations.keys()]
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to initialize MCP integrations: {e}",
                "initialized_servers": len(self.integrations),
                "server_status": {k.value: v.value for k, v in self.server_status.items()}
            }
    
    def get_server_status(self) -> Dict[str, Any]:
        """Get status of all MCP servers"""
        return {
            "success": True,
            "total_servers": len(self.integrations),
            "connected_servers": sum(1 for status in self.server_status.values() 
                                   if status == MCPServerStatus.CONNECTED),
            "server_details": {
                server.value: {
                    "status": status.value,
                    "available": status == MCPServerStatus.CONNECTED
                }
                for server, status in self.server_status.items()
            }
        }
    
    def execute_tavily_search(self, query: str, **kwargs) -> Dict[str, Any]:
        """Execute Tavily search operation"""
        if MCPServerType.TAVILY_EXPERT in self.integrations:
            return self.integrations[MCPServerType.TAVILY_EXPERT].search(query, **kwargs)
        return {"success": False, "error": "Tavily integration not available"}
    
    def execute_context7_docs(self, library_name: str, topic: str, **kwargs) -> Dict[str, Any]:
        """Execute Context7 documentation retrieval"""
        if MCPServerType.CONTEXT7 in self.integrations:
            return self.integrations[MCPServerType.CONTEXT7].get_library_docs(
                library_name, topic, **kwargs
            )
        return {"success": False, "error": "Context7 integration not available"}
    
    def execute_deepwiki_analysis(self, repo_name: str, **kwargs) -> Dict[str, Any]:
        """Execute DeepWiki repository analysis"""
        if MCPServerType.DEEPWIKI in self.integrations:
            return self.integrations[MCPServerType.DEEPWIKI].analyze_repository(
                repo_name, **kwargs
            )
        return {"success": False, "error": "DeepWiki integration not available"}
    
    def execute_fetch_url(self, url: str, **kwargs) -> Dict[str, Any]:
        """Execute URL fetching operation"""
        if MCPServerType.FETCH in self.integrations:
            return self.integrations[MCPServerType.FETCH].fetch_url(url, **kwargs)
        return {"success": False, "error": "Fetch integration not available"}
    
    def shutdown_all_servers(self) -> Dict[str, Any]:
        """Gracefully shutdown all MCP servers"""
        try:
            # Disconnect all servers
            for server_type in list(self.integrations.keys()):
                if hasattr(self.integrations[server_type], 'mcp_manager'):
                    self.integrations[server_type].mcp_manager.disconnect_server(server_type)
                self.server_status[server_type] = MCPServerStatus.DISCONNECTED
            
            self.integrations.clear()
            
            return {
                "success": True,
                "message": "All MCP servers disconnected",
                "disconnected_servers": len(self.server_status)
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to shutdown servers: {e}",
                "disconnected_servers": sum(1 for status in self.server_status.values() 
                                          if status == MCPServerStatus.DISCONNECTED)
            }


def create_mcp_orchestrator() -> MCPOrchestrator:
    """Factory function to create MCP orchestrator"""
    orchestrator = MCPOrchestrator()
    orchestrator.initialize_all_integrations()
    return orchestrator