import subprocess
from agent.reasoning.root_cause_engine import get_root_cause


def run_kubectl_command(command):
    """
    Helper function to run kubectl commands safely.
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


def show_pod_status():
    """
    Display all pod status.
    """

    print("\n 📋 Pod Status:\n")

    output = run_kubectl_command(
        ["kubectl", "get", "pods"]
    )

    print(output)


def show_failing_pods():
    """
    Show only failing pods.
    """

    print("\n 🚨 Failing Pods:\n")

    output = run_kubectl_command(
        ["kubectl", "get", "pods"]
    )

    lines = output.split("\n")

    for line in lines[1:]:

        if line.strip() == "":
            continue

        parts = line.split()

        if len(parts) < 3:
            continue

        pod_name = parts[0]
        status = parts[2]

        if status in ["Error", "CrashLoopBackOff"]:

            print(f"⚠️ {pod_name} → {status}")


def show_memory_usage():
    """
    Display pod memory usage.
    """

    print("\n 📊 Memory Usage:\n")

    output = run_kubectl_command(
        ["kubectl", "top", "pods"]
    )

    print(output)


def show_logs(pod_name):
    """
    Show logs of a specific pod.
    """

    print(f"\n 📜 Logs for {pod_name}:\n")

    output = run_kubectl_command(
        ["kubectl", "logs", pod_name]
    )

    print(output)


def explain_failures():
    """
    Provide readable explanation of failures.
    """

    print("\n 🔎 Failure Reasons:\n")

    output = run_kubectl_command(
        ["kubectl", "get", "pods"]
    )

    lines = output.split("\n")

    for line in lines[1:]:

        if line.strip() == "":
            continue

        parts = line.split()

        if len(parts) < 3:
            continue

        pod_name = parts[0]
        status = parts[2]

        if status == "CrashLoopBackOff":

            print(
                f"⚠️ {pod_name} failing — "
                f"container crashing repeatedly (CrashLoopBackOff)"
            )

        elif status == "Error":

            print(
                f"⚠️ {pod_name} failing — "
                f"application startup error detected"
            )


def start_ai_assistant():
    """
    Main CLI assistant loop.
    """

    print("\n🤖 AI Ops Assistant Ready!")
    print("Type 'exit' to quit.\n")

    while True:

        user_input = input("Ask AI Ops > ").lower()

        if user_input == "exit":

            print("👋 Exiting AI Ops Assistant...")
            break

        elif "pod status" in user_input:

            show_pod_status()

        elif "failing pods" in user_input:

            show_failing_pods()

        elif "memory" in user_input:

            show_memory_usage()

        elif "logs pod" in user_input:

            parts = user_input.split()

            if len(parts) >= 3:

                pod_name = parts[2]
                show_logs(pod_name)

            else:

                print(
                    "\n⚠️ Usage: logs pod <pod-name>\n"
                )

        elif "why" in user_input:

            explain_failures()

        elif "reason" in user_input:

            explain_failures()

        elif "root cause" in user_input:

            issues = get_root_cause()

            print("\n 🚨 Root Cause Analysis:\n")

            for issue in issues:

                print(issue)

        else:

            print(
                "\n 🤖 I can help with:\n"
                "- pod status\n"
                "- failing pods\n"
                "- logs pod <pod-name>\n"
                "- memory usage\n"
                "- why pods failing\n"
                "- root cause\n"
            )
