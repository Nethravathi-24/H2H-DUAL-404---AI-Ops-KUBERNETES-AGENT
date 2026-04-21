import subprocess


def get_pods():
    """
    Get pod list and status
    """

    try:
        result = subprocess.run(
            ["kubectl", "get", "pods"],
            capture_output=True,
            text=True
        )

        lines = result.stdout.split("\n")

        pods = []

        # Skip header
        for line in lines[1:]:

            if line.strip() == "":
                continue

            parts = line.split()

            pod_name = parts[0]
            status = parts[2]

            pods.append({
                "name": pod_name,
                "status": status
            })

        return pods

    except Exception as e:
        print("Error fetching pods:", e)
        return []