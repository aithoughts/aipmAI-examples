from crewai_tools import BaseTool


class MyCustomTool(BaseTool):
    name: str = "我的工具名称"  # 工具名称
    description: str = (
        "对该工具用途的清晰描述，您的代理将需要此信息才能使用它。"
    )

    def _run(self, argument: str) -> str:
        # 实现代码写在这里
        return "这是一个工具输出示例，忽略它并继续。"