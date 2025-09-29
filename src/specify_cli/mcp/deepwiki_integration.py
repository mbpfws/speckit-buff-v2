"""
DeepWiki MCP Server Integration

Provides GitHub repository documentation and analysis through DeepWiki MCP server
for enhanced AI coding workflows across all 10 supported platforms.
"""
from typing import Dict, Any, Optional
from ..mcp import MCPServerType, MCPServerConfig, MCPIntegrationManager


class DeepWikiIntegration:
    """
    Integration with DeepWiki MCP server for GitHub repository documentation and analysis
    """
    
    def __init__(self, mcp_manager: MCPIntegrationManager):
        self.mcp_manager = mcp_manager
        self.server_type = MCPServerType.DEEPWIKI
        
    def read_wiki_structure(self, repo_name: str) -> Dict[str, Any]:
        """Get documentation topics for a GitHub repository"""
        try:
            result = self.mcp_manager.execute_tool(
                self.server_type,
                "read_wiki_structure",
                {"repoName": repo_name}
            )
            return result
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to read wiki structure: {e}",
                "server": self.server_type.value
            }
    
    def read_wiki_contents(self, repo_name: str) -> Dict[str, Any]:
        """View documentation about a GitHub repository"""
        try:
            result = self.mcp_manager.execute_tool(
                self.server_type,
                "read_wiki_contents",
                {"repoName": repo_name}
            )
            return result
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to read wiki contents: {e}",
                "server": self.server_type.value
            }
    
    def ask_question(self, repo_name: str, question: str) -> Dict[str, Any]:
        """Ask questions about a GitHub repository"""
        try:
            result = self.mcp_manager.execute_tool(
                self.server_type,
                "ask_question",
                {
                    "repoName": repo_name,
                    "question": question
                }
            )
            return result
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to ask question: {e}",
                "server": self.server_type.value
            }
    
    def analyze_github_repo(self, repo_name: str) -> Dict[str, Any]:
        """Comprehensive analysis of a GitHub repository"""
        # Get wiki structure first
        structure_result = self.read_wiki_structure(repo_name)
        if not structure_result.get("success", False):
            return structure_result
            
        # Get wiki contents
        contents_result = self.read_wiki_contents(repo_name)
        if not contents_result.get("success", False):
            return contents_result
            
        # Ask specific questions about the repository
        questions = [
            "What is the main purpose of this repository?",
            "What are the key features and capabilities?",
            "What technologies and frameworks are used?"
        ]
        
        answers = {}
        for question in questions:
            answer_result = self.ask_question(repo_name, question)
            if answer_result.get("success", False):
                answers[question] = answer_result.get("result", {})
                
        return {
            "success": True,
            "repo_name": repo_name,
            "structure": structure_result.get("result", {}),
            "contents": contents_result.get("result", {}),
            "qa": answers
        }


def create_deepwiki_integration() -> DeepWikiIntegration:
    """Factory function to create DeepWiki integration"""
    mcp_manager = MCPIntegrationManager()
    
    # Register DeepWiki configuration
    deepwiki_config = MCPServerConfig(
        server_type=MCPServerType.DEEPWIKI,
        endpoint="npx -y mcp-remote https://mcp.deepwiki.com/sse",
        timeout=45
    )
    mcp_manager.register_server(deepwiki_config)
    
    # Connect to server
    mcp_manager.connect_server(MCPServerType.DEEPWIKI)
    
    return DeepWikiIntegration(mcp_manager)