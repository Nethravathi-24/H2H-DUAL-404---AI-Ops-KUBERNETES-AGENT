import subprocess


def get_pod_logs(pod_name):
    """
    Fetch logs from a pod
    """
    try:
        result = subprocess.run(
            ["kubectl", "logs", pod_name],
            capture_output=True,
            text=True
        )

        return result.stdout

    except Exception as e:
        return str(e)
