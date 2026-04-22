import subprocess
from agent.reasoning.root_cause_engine import get_root_cause


def run_kubectl_command(command):
    """
    Safely run kubectl commands.
    """

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        return result.stdout

    except Exception as e:
        return str(e)


def process_query(query):
    """
    Natural language query processor.
    """

    query = query.lower()

    # ----------------------------
    # POD STATUS
    # ----------------------------
    if "pod status" in query:

        output = run_kubectl_command(
            ["kubectl", "get", "pods"]
        )

        return f"\n 📋 Pod Status:\n\n{output}"

    # ----------------------------
    # FAILING PODS
    # ----------------------------
    elif "failing pods" in query:

        output = run_kubectl_command(
            ["kubectl", "get", "pods"]
        )

        lines = output.split("\n")

        response = "\n 🚨 Failing Pods:\n\n"

        for line in lines[1:]:

            if line.strip() == "":
                continue

            parts = line.split()

            if len(parts) < 3:
                continue

            pod_name = parts[0]
            status = parts[2]

            if status in ["Error", "CrashLoopBackOff"]:

                response += f"⚠️ {pod_name} → {status}\n"

        return response

    # ----------------------------
    # MEMORY USAGE
    # ----------------------------
    elif "memory" in query:

        output = run_kubectl_command(
            ["kubectl", "top", "pods"]
        )

        return f"\n 📊 Memory Usage:\n\n{output}"

    # ----------------------------
    # LOGS COMMAND
    # ----------------------------
    elif "logs pod" in query:

        parts = query.split()

        if len(parts) >= 3:

            pod_name = parts[2]

            output = run_kubectl_command(
                ["kubectl", "logs", pod_name]
            )

            return f"\n 📜 Logs for {pod_name}:\n\n{output}"

        else:

            return "\n⚠️ Usage: logs pod <pod-name>\n"

    # ----------------------------
    # WHY PODS FAILING
    # ----------------------------
    elif "why" in query:

        output = run_kubectl_command(
            ["kubectl", "get", "pods"]
        )

        lines = output.split("\n")

        response = "\n 🔎 Failure Reasons:\n\n"

        for line in lines[1:]:

            if line.strip() == "":
                continue

            parts = line.split()

            if len(parts) < 3:
                continue

            pod_name = parts[0]
            status = parts[2]

            if status == "CrashLoopBackOff":

                response += (
                    f"⚠️ {pod_name} failing — "
                    f"container crashing repeatedly "
                    f"(CrashLoopBackOff)\n"
                )

            elif status == "Error":

                response += (
                    f"⚠️ {pod_name} failing — "
                    f"application startup error detected\n"
                )

        return response

    # ----------------------------
    # ROOT CAUSE (IMPORTANT)
    # ----------------------------
    elif "root cause" in query:

        issues = get_root_cause()

        response = "\n 🚨 Root Cause Analysis:\n\n"

        for issue in issues:

            response += f"{issue}\n"

        return response

    # ----------------------------
    # DEFAULT HELP
    # ----------------------------
    else:

        return (
            "\n 🤖 I can help with:\n"
            "- pod status\n"
            "- failing pods\n"
            "- logs pod <pod-name>\n"
            "- memory usage\n"
            "- why pods failing\n"
            "- root cause\n"
        )
