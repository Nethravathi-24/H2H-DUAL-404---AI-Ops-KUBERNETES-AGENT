import subprocess


def get_pod_logs(pod_name=None):
    """
    Get logs from a specific pod
    """

    try:
        # If pod name not provided, get first pod
        if pod_name is None:
            pod_cmd = ["kubectl", "get", "pods"]

            pod_result = subprocess.run(
                pod_cmd,
                capture_output=True,
                text=True
            )

            lines = pod_result.stdout.split("\n")

            if len(lines) > 1:
                pod_name = lines[1].split()[0]

        # Get logs
        log_cmd = ["kubectl", "logs", pod_name]

        log_result = subprocess.run(
            log_cmd,
            capture_output=True,
            text=True
        )

        return log_result.stdout

    except Exception as e:
        return str(e)
