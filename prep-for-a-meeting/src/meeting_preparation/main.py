from aipm_examples.crew import MeetingPreparationCrew

def run():
   
    # 用您的输入替换，它将自动插入任何任务和代理信息
    # 欢迎信息和用户输入
    print("## 欢迎使用会议准备团队")
    print('-------------------------------')
    meeting_participants = input("除了您之外，参加会议的其他人的电子邮件地址是什么？\n")
    meeting_context = input("会议的背景是什么？\n")
    meeting_objective = input("您参加这次会议的目标是什么？\n")
    inputs = {
        "meeting_participants": meeting_participants,
        "meeting_context": meeting_context,
        "meeting_objective": meeting_objective
        }
    MeetingPreparationCrew().crew().kickoff(inputs=inputs)