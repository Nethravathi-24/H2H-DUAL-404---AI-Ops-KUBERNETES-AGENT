import subprocess


def get_pod_metrics():
    """
    Get pod metrics
    Requires metrics-server
    """
    try:
        result = subprocess.run(
            ["kubectl", "top", "pods"],
            capture_output=True,
            text=True
        )

        return result.stdout

    except Exception as e:
        return str(e)
