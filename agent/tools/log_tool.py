import subprocess


def get_pod_logs(pod_name):
    """
    Fetch logs of a pod.
    Try normal logs first, then previous logs.
    """

    try:
        # Try normal logs
        result = subprocess.run(
            ["kubectl", "logs", pod_name],
            capture_output=True,
            text=True
        )

        logs = result.stdout

        # If empty, try previous logs
        if not logs:

            result_prev = subprocess.run(
                ["kubectl", "logs", pod_name, "--previous"],
                capture_output=True,
                text=True
            )

            logs = result_prev.stdout

        return logs

    except Exception as e:
        return str(e)