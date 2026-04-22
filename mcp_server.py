from fastmcp import FastMCP
import subprocess  # package that can run commands on terminal


mcp = FastMCP("Docker mcp server")  # instance


def _run_docker_command(*args):
    result = subprocess.run(
        ["docker", *args],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        return result.stdout
    return result.stderr or result.stdout or f"docker command failed: {result.returncode}"


@mcp.tool
def show_running_containers():
    """Show currently running Docker containers."""
    return _run_docker_command("ps")


@mcp.tool
def show_containers_logs(container_name):
    """Fetch logs of a specific Docker container."""
    return _run_docker_command("logs", "--tail", "50", container_name)


@mcp.tool
def show_all_containers():
    """List all Docker containers (running and stopped)."""
    return _run_docker_command("ps", "-a")


if __name__ == "__main__":
    mcp.run(transport="stdio", show_banner=False)
