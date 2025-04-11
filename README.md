# OpenWebUI Frontend URLs

*Last Updated: April 11, 2025*

## Purpose

This one-page repository compiles front-end URLs for OpenWebUI. The aim is to simplify the setup of advanced wrappers, clients, and multi-tiled window displays. Some functionalities may not have a unique URL right now, and the URL construction pattern is included where possible, especially regarding the ID value in the model table.

## URL Reference Table

| Section | Function | URL Pattern | Notes |
|---------|----------|-------------|-------|
| **General** | Home | `https://yourinstanceurl.com/` | Base URL |
| **Models** | Models Home | `https://yourinstanceurl.com/workspace/models` | List all models |
| | Chat with Specific Model | `https://yourinstanceurl.com/?models=ai-assistant-platform` | Chat UI prepopulated with model |
| | Edit Model | `https://yourinstanceurl.com/workspace/models/edit?id=ai-assistant-platform` | Where `id` = value from model table in database |
| | Create New Model | `https://yourinstanceurl.com/workspace/models/create` | |
| **Knowledge** | Knowledge Home | `https://yourinstanceurl.com/workspace/knowledge` | List all knowledge collections |
| | Create Knowledge | `https://yourinstanceurl.com/workspace/knowledge/create` | |
| | View Knowledge | `https://yourinstanceurl.com/workspace/knowledge/a1b2c3d4-e5f6-7890-1234-567890abcdef` | Where `id` = UUID of document collection |
| **Prompts** | Prompts Home | `https://yourinstanceurl.com/workspace/prompts` | |
| | Create Prompt | `https://yourinstanceurl.com/workspace/prompts/create` | |
| | Edit Prompt | `https://yourinstanceurl.com/workspace/prompts/edit?command=%2Fmy-hardware-specs` | URL based on command line value, not prompt name |
| **Tools** | Tools Home | `https://yourinstanceurl.com/workspace/tools` | |
| | Edit Tool | `https://yourinstanceurl.com/workspace/tools/edit?id=postgres_database_tool` | Where `id` = tool ID in your instance |
| **Admin** | Settings | `https://yourinstanceurl.com/admin/settings` | |
| | User Management | `https://yourinstanceurl.com/admin/users` | |
| | Evaluations | `https://yourinstanceurl.com/admin/evaluations` | |
| **Functions** | Functions List | `https://yourinstanceurl.com/admin/functions` | |
| | Edit Function | `https://yourinstanceurl.com/admin/functions/edit?id=add_to_knowledge_action` | Where `id` = function ID |
| | Playground | `https://yourinstanceurl.com/playground` | |
| | Completions Tester | `https://yourinstanceurl.com/playground/completions` | |
| **Conversations** | View Chat History | `https://yourinstanceurl.com/c/a1b2c3d4-e5f6-7890-1234-567890abcdef` | Where `id` = chat UUID |
