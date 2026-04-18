import subprocess


def run_kubectl_command(command):
    """
    Runs kubectl command safely
    """
    try:
        result = subprocess.run(
            ["kubectl"] + command,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return result.stdout
        else:
            return result.stderr

    except Exception as e:
        return str(e)


def get_pods():
    """Get all pods"""
    return run_kubectl_command(["get", "pods", "-o", "wide"])


def get_nodes():
    """Get cluster nodes"""
    return run_kubectl_command(["get", "nodes"])


def describe_pod(pod_name):
    """Describe specific pod"""
    return run_kubectl_command(
        ["describe", "pod", pod_name]
    )


def delete_pod(pod_name):
    """Restart pod by deleting"""
    return run_kubectl_command(
        ["delete", "pod", pod_name]
    )
