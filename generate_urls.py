#!/usr/bin/env python3
"""
OpenWebUI URL Generator

This script generates a markdown file with all OpenWebUI frontend URLs
customized for a specific instance URL provided by the user.
"""

import os
import sys
import json
import datetime
from urllib.parse import urlparse

def validate_url(url):
    """Validate and normalize the instance URL."""
    # Add https:// if no scheme is provided
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # Remove trailing slash if present
    parsed = urlparse(url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    
    return base_url

def generate_markdown(instance_url):
    """Generate markdown content with all URLs for the given instance."""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Example model and function IDs - these would be specific to the user's instance
    model_id = "ai-assistant-platform"
    tool_id = "postgres_database_tool"
    function_id = "add_to_knowledge_action"
    knowledge_uuid = "a1b2c3d4-e5f6-7890-1234-567890abcdef"
    chat_uuid = "a1b2c3d4-e5f6-7890-1234-567890abcdef"
    
    markdown = f"""# OpenWebUI URLs for {instance_url}

*Generated on: {today}*

## URL Reference Table

| Section | Function | URL |
|---------|----------|-----|
| **General** | Home | `{instance_url}/` |
| **Models** | Models Home | `{instance_url}/workspace/models` |
| | Chat with Specific Model | `{instance_url}/?models={model_id}` |
| | Edit Model | `{instance_url}/workspace/models/edit?id={model_id}` |
| | Create New Model | `{instance_url}/workspace/models/create` |
| **Knowledge** | Knowledge Home | `{instance_url}/workspace/knowledge` |
| | Create Knowledge | `{instance_url}/workspace/knowledge/create` |
| | View Knowledge | `{instance_url}/workspace/knowledge/{knowledge_uuid}` |
| **Prompts** | Prompts Home | `{instance_url}/workspace/prompts` |
| | Create Prompt | `{instance_url}/workspace/prompts/create` |
| | Edit Prompt | `{instance_url}/workspace/prompts/edit?command=%2Fmy-hardware-specs` |
| **Tools** | Tools Home | `{instance_url}/workspace/tools` |
| | Edit Tool | `{instance_url}/workspace/tools/edit?id={tool_id}` |
| **Admin** | Settings | `{instance_url}/admin/settings` |
| | User Management | `{instance_url}/admin/users` |
| | Evaluations | `{instance_url}/admin/evaluations` |
| **Functions** | Functions List | `{instance_url}/admin/functions` |
| | Edit Function | `{instance_url}/admin/functions/edit?id={function_id}` |
| | Playground | `{instance_url}/playground` |
| | Completions Tester | `{instance_url}/playground/completions` |
| **Conversations** | View Chat History | `{instance_url}/c/{chat_uuid}` |

## Notes

- For model-specific URLs, replace `{model_id}` with the actual model ID from your database
- For knowledge document URLs, replace `{knowledge_uuid}` with the actual UUID of the document collection
- For tool-specific URLs, replace `{tool_id}` with the actual tool ID from your instance
- For function-specific URLs, replace `{function_id}` with the actual function ID
- For chat history URLs, replace `{chat_uuid}` with the actual chat UUID
"""
    return markdown

def generate_json(instance_url):
    """Generate JSON content with all URLs for the given instance."""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Example model and function IDs - these would be specific to the user's instance
    model_id = "ai-assistant-platform"
    tool_id = "postgres_database_tool"
    function_id = "add_to_knowledge_action"
    knowledge_uuid = "a1b2c3d4-e5f6-7890-1234-567890abcdef"
    chat_uuid = "a1b2c3d4-e5f6-7890-1234-567890abcdef"
    
    json_data = {
        "metadata": {
            "lastUpdated": today,
            "description": "OpenWebUI frontend URLs for simplifying setup of advanced wrappers, clients, and multi-tiled window displays",
            "instanceUrl": instance_url
        },
        "baseUrl": instance_url,
        "sections": [
            {
                "name": "General",
                "endpoints": [
                    {
                        "function": "Home",
                        "urlPattern": "/",
                        "fullUrl": f"{instance_url}/",
                        "notes": "Base URL"
                    }
                ]
            },
            {
                "name": "Models",
                "endpoints": [
                    {
                        "function": "Models Home",
                        "urlPattern": "/workspace/models",
                        "fullUrl": f"{instance_url}/workspace/models",
                        "notes": "List all models"
                    },
                    {
                        "function": "Chat with Specific Model",
                        "urlPattern": "/?models={modelId}",
                        "fullUrl": f"{instance_url}/?models={model_id}",
                        "notes": "Chat UI prepopulated with model",
                        "parameters": [
                            {
                                "name": "modelId",
                                "description": "The ID value from the model table in database",
                                "example": model_id
                            }
                        ]
                    },
                    {
                        "function": "Edit Model",
                        "urlPattern": "/workspace/models/edit?id={modelId}",
                        "fullUrl": f"{instance_url}/workspace/models/edit?id={model_id}",
                        "notes": "Edit a specific model",
                        "parameters": [
                            {
                                "name": "modelId",
                                "description": "The ID value from the model table in database",
                                "example": model_id
                            }
                        ]
                    },
                    {
                        "function": "Create New Model",
                        "urlPattern": "/workspace/models/create",
                        "fullUrl": f"{instance_url}/workspace/models/create",
                        "notes": "Create a new model"
                    }
                ]
            },
            {
                "name": "Knowledge",
                "endpoints": [
                    {
                        "function": "Knowledge Home",
                        "urlPattern": "/workspace/knowledge",
                        "fullUrl": f"{instance_url}/workspace/knowledge",
                        "notes": "List all knowledge collections"
                    },
                    {
                        "function": "Create Knowledge",
                        "urlPattern": "/workspace/knowledge/create",
                        "fullUrl": f"{instance_url}/workspace/knowledge/create",
                        "notes": "Create a new knowledge collection"
                    },
                    {
                        "function": "View Knowledge",
                        "urlPattern": "/workspace/knowledge/{knowledgeId}",
                        "fullUrl": f"{instance_url}/workspace/knowledge/{knowledge_uuid}",
                        "notes": "View a specific knowledge collection",
                        "parameters": [
                            {
                                "name": "knowledgeId",
                                "description": "UUID of the document collection",
                                "example": knowledge_uuid
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Prompts",
                "endpoints": [
                    {
                        "function": "Prompts Home",
                        "urlPattern": "/workspace/prompts",
                        "fullUrl": f"{instance_url}/workspace/prompts",
                        "notes": "List all prompts"
                    },
                    {
                        "function": "Create Prompt",
                        "urlPattern": "/workspace/prompts/create",
                        "fullUrl": f"{instance_url}/workspace/prompts/create",
                        "notes": "Create a new prompt"
                    },
                    {
                        "function": "Edit Prompt",
                        "urlPattern": "/workspace/prompts/edit?command={commandValue}",
                        "fullUrl": f"{instance_url}/workspace/prompts/edit?command=%2Fmy-hardware-specs",
                        "notes": "URL based on command line value, not prompt name",
                        "parameters": [
                            {
                                "name": "commandValue",
                                "description": "The command line value for the prompt",
                                "example": "%2Fmy-hardware-specs"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Tools",
                "endpoints": [
                    {
                        "function": "Tools Home",
                        "urlPattern": "/workspace/tools",
                        "fullUrl": f"{instance_url}/workspace/tools",
                        "notes": "List all tools"
                    },
                    {
                        "function": "Edit Tool",
                        "urlPattern": "/workspace/tools/edit?id={toolId}",
                        "fullUrl": f"{instance_url}/workspace/tools/edit?id={tool_id}",
                        "notes": "Edit a specific tool",
                        "parameters": [
                            {
                                "name": "toolId",
                                "description": "Tool ID in your instance",
                                "example": tool_id
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Admin",
                "endpoints": [
                    {
                        "function": "Settings",
                        "urlPattern": "/admin/settings",
                        "fullUrl": f"{instance_url}/admin/settings",
                        "notes": "Admin settings"
                    },
                    {
                        "function": "User Management",
                        "urlPattern": "/admin/users",
                        "fullUrl": f"{instance_url}/admin/users",
                        "notes": "Manage users"
                    },
                    {
                        "function": "Evaluations",
                        "urlPattern": "/admin/evaluations",
                        "fullUrl": f"{instance_url}/admin/evaluations",
                        "notes": "View evaluations"
                    }
                ]
            },
            {
                "name": "Functions",
                "endpoints": [
                    {
                        "function": "Functions List",
                        "urlPattern": "/admin/functions",
                        "fullUrl": f"{instance_url}/admin/functions",
                        "notes": "List all functions"
                    },
                    {
                        "function": "Edit Function",
                        "urlPattern": "/admin/functions/edit?id={functionId}",
                        "fullUrl": f"{instance_url}/admin/functions/edit?id={function_id}",
                        "notes": "Edit a specific function",
                        "parameters": [
                            {
                                "name": "functionId",
                                "description": "Function ID",
                                "example": function_id
                            }
                        ]
                    },
                    {
                        "function": "Playground",
                        "urlPattern": "/playground",
                        "fullUrl": f"{instance_url}/playground",
                        "notes": "Function playground"
                    },
                    {
                        "function": "Completions Tester",
                        "urlPattern": "/playground/completions",
                        "fullUrl": f"{instance_url}/playground/completions",
                        "notes": "Test completions"
                    }
                ]
            },
            {
                "name": "Conversations",
                "endpoints": [
                    {
                        "function": "View Chat History",
                        "urlPattern": "/c/{chatId}",
                        "fullUrl": f"{instance_url}/c/{chat_uuid}",
                        "notes": "View a specific chat history",
                        "parameters": [
                            {
                                "name": "chatId",
                                "description": "Chat UUID",
                                "example": chat_uuid
                            }
                        ]
                    }
                ]
            }
        ]
    }
    
    return json.dumps(json_data, indent=2)

def save_markdown(content, instance_name):
    """Save the generated markdown to a file."""
    # Create a sanitized filename from the instance name
    filename = instance_name.replace('https://', '').replace('http://', '').replace('/', '-').replace(':', '-')
    output_file = f"owui-urls-{filename}.md"
    
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"Markdown URLs have been saved to {output_file}")
    return output_file

def save_json(content, instance_name):
    """Save the generated JSON to a file."""
    # Create a sanitized filename from the instance name
    filename = instance_name.replace('https://', '').replace('http://', '').replace('/', '-').replace(':', '-')
    output_file = f"owui-urls-{filename}.json"
    
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"JSON URLs have been saved to {output_file}")
    return output_file

def main():
    """Main function to run the script."""
    print("OpenWebUI URL Generator")
    print("======================")
    
    if len(sys.argv) > 1:
        instance_url = sys.argv[1]
    else:
        instance_url = input("Enter your OpenWebUI instance URL (e.g., chat.example.com): ")
    
    # Validate and normalize the URL
    instance_url = validate_url(instance_url)
    
    # Ask for output format
    format_choice = input("Choose output format (1 for Markdown, 2 for JSON, 3 for both) [3]: ").strip() or "3"
    
    md_file = None
    json_file = None
    
    if format_choice in ["1", "3"]:
        # Generate the markdown content
        markdown_content = generate_markdown(instance_url)
        md_file = save_markdown(markdown_content, instance_url)
    
    if format_choice in ["2", "3"]:
        # Generate the JSON content
        json_content = generate_json(instance_url)
        json_file = save_json(json_content, instance_url)
    
    print("\nSuccess! Your OpenWebUI URLs have been generated.")
    if md_file:
        print(f"Markdown: {os.path.abspath(md_file)}")
    if json_file:
        print(f"JSON: {os.path.abspath(json_file)}")

if __name__ == "__main__":
    main()
