from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# 取消注释以下行以使用自定义工具示例
# from marketing_posts.tools.custom_tool import MyCustomTool

# 查看我们的工具文档以获取有关如何使用它们的更多信息
from crewai_tools import SerperDevTool
from pydantic import BaseModel, Field

# 取消注释以下行以使用Ollama
# from langchain_community.llms import Ollama
# import os
# os.environ["OPENAI_API_KEY"] = "NA"

# llm = Ollama(
#     model = "llama3.1",
#     base_url = "http://localhost:11434")

@CrewBase
class MeetingPreparationCrew():

	agents_config = 'config/agents.yaml'

	@agent
	def research_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['research_agent'],
			tools=[SerperDevTool()],
			verbose=True,
			max_rpm=15,
			memory=False,
			# llm = llm
		)

	@agent
	def industry_analysis_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['industry_analysis_agent'],
			tools=[SerperDevTool()],
			verbose=True,
			max_rpm=15,
			memory=False,
			# llm = llm
		)

	@agent
	def meeting_strategy_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['meeting_strategy_agent'],
			# tools=[SerperDevTool()],
			verbose=True,
			max_rpm=15,
			memory=False,
			# llm = llm
		)
	
	@agent
	def summary_and_briefing_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['summary_and_briefing_agent'],
			# tools=[SerperDevTool()],
			verbose=True,
			max_rpm=15,
			memory=False,
			# llm = llm
		)
	
	tasks_config = 'config/tasks.yaml'

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			agent=self.research_agent(),
			async_execution=True
		)

	@task
	def industry_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['industry_analysis_task'],
			agent=self.industry_analysis_agent(),
			async_execution=True
		)

	@task
	def meeting_strategy_task(self) -> Task:
		return Task(
			config=self.tasks_config['meeting_strategy_task'],
			agent=self.meeting_strategy_agent(),
			context=[self.research_task(), self.industry_analysis_task()],
		)
	
	@task
	def summary_and_briefing_task(self) -> Task:
		return Task(
			config=self.tasks_config['summary_and_briefing_task'],
			agent=self.summary_and_briefing_agent(),
			context=[self.research_task(), self.industry_analysis_task(),self.meeting_strategy_task()],
		)

	@crew
	def crew(self) -> Crew:
		"""创建会议筹备团队"""
		return Crew(
			agents=self.agents, # 由 @agent 装饰器自动创建
			tasks=self.tasks, # 由 @task 装饰器自动创建
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # 如果您想改用它 https://aipmai.theforage.cn/how-to/Hierarchical/
		)
