import subprocess


def get_pod_metrics():
    """
    Get CPU and Memory usage using kubectl top
    """

    try:
        result = subprocess.run(
            ["kubectl", "top", "pods"],
            capture_output=True,
            text=True
        )

        output = result.stdout

        if "error" in output.lower():
            return "Metrics not available. Install metrics-server."

        lines = output.split("\n")

        metrics = []

        # Skip header
        for line in lines[1:]:

            if line.strip() == "":
                continue

            parts = line.split()

            pod_name = parts[0]
            cpu = parts[1]
            memory = parts[2]

            metrics.append({
                "name": pod_name,
                "cpu": cpu,
                "memory": memory
            })

        return metrics

    except Exception as e:
        return str(e)