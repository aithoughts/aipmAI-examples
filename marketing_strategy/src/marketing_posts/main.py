#!/usr/bin/env python
import sys
from marketing_posts.crew import MarketingPostsCrew


def run():
    # 用您的输入替换，它将自动插入任何任务和代理信息
    inputs = {
        'customer_domain': 'crewai.com',
        'project_description': """
        CrewAI 是一家领先的多代理系统提供商，旨在为其企业客户彻底改变营销自动化。 该项目涉及制定一项创新的营销策略，以展示 CrewAI 先进的 AI 驱动解决方案，强调易用性、可扩展性和集成能力。 该活动将针对大中型企业的技术娴熟的决策者，重点介绍成功案例和 CrewAI 平台的变革潜力。
        
        客户领域：人工智能和自动化解决方案
        项目概述：创建一项全面的营销活动，以提高企业客户对 CrewAI 服务的认识和采用率。
        """
    }
    MarketingPostsCrew().crew().kickoff(inputs=inputs)


def train():
    """
    训练团队指定的迭代次数。
    """
    inputs = {
        'customer_domain': 'crewai.com',
        'project_description': """
        CrewAI 是一家领先的多代理系统提供商，旨在为其企业客户彻底改变营销自动化。 该项目涉及制定一项创新的营销策略，以展示 CrewAI 先进的 AI 驱动解决方案，强调易用性、可扩展性和集成能力。 该活动将针对大中型企业的技术娴熟的决策者，重点介绍成功案例和 CrewAI 平台的变革潜力。
        
        客户领域：人工智能和自动化解决方案
        项目概述：创建一项全面的营销活动，以提高企业客户对 CrewAI 服务的认识和采用率。
        """
    }
    try:
        MarketingPostsCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"训练团队时出错：{e}")
