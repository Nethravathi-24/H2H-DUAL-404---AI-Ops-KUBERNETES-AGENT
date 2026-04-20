import subprocess


def get_cluster_summary():

    try:

        result = subprocess.run(
            ["kubectl", "get", "pods"],
            capture_output=True,
            text=True
        )

        output = result.stdout

        lines = output.split("\n")

        total = 0
        running = 0
        failing = 0

        for line in lines[1:]:

            if line.strip() == "":
                continue

            parts = line.split()

            if len(parts) < 3:
                continue

            status = parts[2]

            total += 1

            if status == "Running":
                running += 1
            else:
                failing += 1

        return {
            "total": total,
            "running": running,
            "failing": failing
        }

    except Exception as e:

        return {
            "total": 0,
            "running": 0,
            "failing": 0
        }