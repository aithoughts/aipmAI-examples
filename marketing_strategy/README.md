# 用于营销策略的 AI 团队

## 简介

本项目演示了如何使用 CrewAI 框架来自动创建营销策略。CrewAI 对自主 AI 代理进行编排，使其能够高效地协作和执行复杂的任务。

- [CrewAI 框架](#crewai-框架)
- [运行脚本](#运行脚本)
- [详细信息和说明](#详细信息和说明)
- [贡献](#贡献)
- [支持和联系](#支持和联系)
- [许可证](#许可证)

## CrewAI 框架
CrewAI 旨在促进扮演不同角色的 AI 代理之间的协作。在本示例中，这些代理协同工作以创建全面的营销策略并开发引人注目的营销内容。

## 运行脚本
本项目可采用两种方式运行。
1） 通过Ollama运行本地大型语言模型
2） 通过接口运行云端大型语言模型

- **配置环境**：复制 `.env.example` 并根据需要设置 [OpenAI](https://platform.openai.com/api-keys) 和其他工具的环境变量，例如 [Serper](serper.dev)。
- **安装依赖项**：运行 `poetry lock && poetry install`。
- **自定义**：修改 `src/marketing_posts/main.py` 以为您的代理和任务添加自定义输入。
- **进一步自定义**：查看 `src/marketing_posts/config/agents.yaml` 以更新您的代理，并查看 `src/marketing_posts/config/tasks.yaml` 以更新您的任务。
- **执行脚本**：运行 `poetry run marketing_posts` 并输入您的项目详细信息。

## 详细信息和说明
- **运行脚本**：执行 `poetry run marketing_posts`。该脚本将利用 CrewAI 框架生成详细的营销策略。
- **关键组件**：
  - `src/marketing_posts/main.py`：主脚本文件。
  - `src/marketing_posts/crew.py`：主要的团队文件，代理和任务在此汇集，主要逻辑在此执行。
  - `src/marketing_posts/config/agents.yaml`：用于定义代理的配置文件。
  - `src/marketing_posts/config/tasks.yaml`：用于定义任务的配置文件。
  - `src/marketing_posts/tools`：包含代理使用的工具类。

## 许可证
本项目根据 MIT 许可证发布。
