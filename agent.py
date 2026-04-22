from langchain_ollama import ChatOllama
import subprocess # package that can run commands on termi nal
from langchain_core.tools import tool
from langchain.agents import create_agent

System_prompt = """
You are docker expert and you can explain things in one two lines max. you don't overthink and hallucinate and keep reasoning and u keep reason and act accordigy
below things you tell
1.you tell about errors
2.you tell about solution 
3.you tell about root cause 
"""

@tool
def show_running_containers():
    """Show currently running Docker containers."""
    result = subprocess.run(["docker","ps"],capture_output=True,text=True)
    return result.stdout

@tool
def show_containers_logs(container_name):
    """Fetch logs of a specific Docker container."""
    result = subprocess.run(["docker","logs","--tail","50",container_name],capture_output=True,text=True)
    return result.stdout

@tool
def show_all_containers():
    """List all Docker containers (running and stopped)."""
    result = subprocess.run(["docker","ps","-a"],capture_output=True,text=True)
    return result.stdout

model = ChatOllama(model="gpt-oss:120b-cloud",temperature="0.8",system=System_prompt) #LLM
tools = [show_all_containers,show_containers_logs,show_containers_logs] #Tools

agent = create_agent(model,tools);

 
while True:
    user_input = input("enter the message:\n");
    if user_input == "exit":
        break
    responce = agent.invoke({"messages" : [{'role': 'user','content': user_input,}]})
    print(responce['messages'][-1].content)