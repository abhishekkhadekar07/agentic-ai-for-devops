from langchain_ollama import ChatOllama
import subprocess # package that can run commands on termi nal
from langchain_core.tools import tool
from langchain.agents import create_agent

System_prompt = """
You are kubernetes expert and you can explain things in one two lines max. you don't overthink and hallucinate and keep reasoning and u keep reason and act accordigy
below things you tell
1.you tell about errors
2.you tell about solution 
3.you tell about root cause 
"""

@tool
def kubectl_get_nodes():
    """Show all Kubernetes cluster nodes."""
    result = subprocess.run(
        ["kubectl", "get", "nodes"],
        capture_output=True,
        text=True
    )
    return result.stdout


@tool
def kubectl_get_pods():
    """Show pods in current namespace."""
    result = subprocess.run(
        ["kubectl", "get", "pods"],
        capture_output=True,
        text=True
    )
    return result.stdout


@tool
def kubectl_get_all_pods():
    """Show pods in all namespaces."""
    result = subprocess.run(
        ["kubectl", "get", "pods", "-A"],
        capture_output=True,
        text=True
    )
    return result.stdout


@tool
def kubectl_get_services():
    """Show all services."""
    result = subprocess.run(
        ["kubectl", "get", "svc"],
        capture_output=True,
        text=True
    )
    return result.stdout


@tool
def kubectl_get_deployments():
    """Show all deployments."""
    result = subprocess.run(
        ["kubectl", "get", "deployments"],
        capture_output=True,
        text=True
    )
    return result.stdout


@tool
def kubectl_get_namespaces():
    """Show all namespaces."""
    result = subprocess.run(
        ["kubectl", "get", "namespaces"],
        capture_output=True,
        text=True
    )
    return result.stdout


@tool
def kubectl_cluster_info():
    """Show Kubernetes cluster information."""
    result = subprocess.run(
        ["kubectl", "cluster-info"],
        capture_output=True,
        text=True
    )
    return result.stdout


@tool
def kubectl_get_all():
    """Show all resources in current namespace."""
    result = subprocess.run(
        ["kubectl", "get", "all"],
        capture_output=True,
        text=True
    )
    return result.stdout


@tool
def minikube_status():
    """Show Minikube cluster status."""
    result = subprocess.run(
        ["minikube", "status"],
        capture_output=True,
        text=True
    )
    return result.stdout

model = ChatOllama(model="gpt-oss:120b-cloud",temperature="0.8",system=System_prompt) #LLM
tools = [
    minikube_status,
    kubectl_cluster_info,
    kubectl_get_nodes,
    kubectl_get_pods,
    kubectl_get_all_pods,
    kubectl_get_services,
    kubectl_get_deployments,
    kubectl_get_namespaces,
    kubectl_get_all,
] #Tools

agent = create_agent(model,tools);

 
while True:
    user_input = input("enter the message:\n");
    if user_input == "exit":
        break
    responce = agent.invoke({"messages" : [{'role': 'user','content': user_input,}]})
    print(responce['messages'][-1].content)