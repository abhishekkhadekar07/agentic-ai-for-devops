import subprocess
from fastmcp import FastMCP

mcp = FastMCP("Kubernetes MCP Server")


def run_cmd(cmd):
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=20
        )
        return result.stdout or result.stderr
    except Exception as e:
        return str(e)


@mcp.tool
def kubectl_get_nodes():
    return run_cmd(["kubectl", "get", "nodes"])


@mcp.tool
def kubectl_get_pods():
    return run_cmd(["kubectl", "get", "pods"])


@mcp.tool
def minikube_status():
    return run_cmd(["minikube", "status"])


if __name__ == "__main__":
    mcp.run(transport="stdio")