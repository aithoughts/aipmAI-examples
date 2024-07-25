from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# 取消注释以下行以使用自定义工具示例
# from marketing_posts.tools.custom_tool import MyCustomTool

# 查看我们的工具文档以获取有关如何使用它们的更多信息
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from pydantic import BaseModel, Field

# 取消注释以下行以使用Ollama
# from langchain_community.llms import Ollama
# import os
# os.environ["OPENAI_API_KEY"] = "NA"

# llm = Ollama(
#     model = "mistral",
#     base_url = "http://localhost:11434")

class MarketStrategy(BaseModel):
	"""市场策略模型"""
	name: str = Field(..., description="市场策略的名称")
	tatics: List[str] = Field(..., description="市场策略中使用的策略列表")
	channels: List[str] = Field(..., description="市场策略中使用的渠道列表")
	KPIs: List[str] = Field(..., description="市场策略中使用的关键绩效指标列表")

class CampaignIdea(BaseModel):
	"""活动创意模型"""
	name: str = Field(..., description="活动创意的名称")
	description: str = Field(..., description="活动创意的描述")
	audience: str = Field(..., description="活动创意的目标受众")
	channel: str = Field(..., description="活动创意的渠道")

class Copy(BaseModel):
	"""文案模型"""
	title: str = Field(..., description="文案标题")
	body: str = Field(..., description="文案正文")

@CrewBase
class MarketingPostsCrew():
	"""营销帖子团队"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def lead_market_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['lead_market_analyst'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			max_iter=10,
			verbose=True,
			memory=False,
			# llm = llm
		)

	@agent
	def chief_marketing_strategist(self) -> Agent:
		return Agent(
			config=self.agents_config['chief_marketing_strategist'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			max_iter=10,
			verbose=True,
			memory=False,
			# llm = llm
		)

	@agent
	def creative_content_creator(self) -> Agent:
		return Agent(
			config=self.agents_config['creative_content_creator'],
			max_iter=10,
			verbose=True,
			memory=False,
			# llm = llm
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			agent=self.lead_market_analyst()
		)

	@task
	def project_understanding_task(self) -> Task:
		return Task(
			config=self.tasks_config['project_understanding_task'],
			agent=self.chief_marketing_strategist()
		)

	@task
	def marketing_strategy_task(self) -> Task:
		return Task(
			config=self.tasks_config['marketing_strategy_task'],
			agent=self.chief_marketing_strategist(),
			output_json=MarketStrategy
		)

	@task
	def campaign_idea_task(self) -> Task:
		return Task(
			config=self.tasks_config['campaign_idea_task'],
			agent=self.creative_content_creator(),
   		output_json=CampaignIdea
		)

	@task
	def copy_creation_task(self) -> Task:
		return Task(
			config=self.tasks_config['copy_creation_task'],
			agent=self.creative_content_creator(),
   		context=[self.marketing_strategy_task(), self.campaign_idea_task()],
			output_json=Copy
		)

	@crew
	def crew(self) -> Crew:
		"""创建营销帖子团队"""
		return Crew(
			agents=self.agents, # 由 @agent 装饰器自动创建
			tasks=self.tasks, # 由 @task 装饰器自动创建
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # 如果您想改用它 https://aipmai.theforage.cn/how-to/Hierarchical/
		)
