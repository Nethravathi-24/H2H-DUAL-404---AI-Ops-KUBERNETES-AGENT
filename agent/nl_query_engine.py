import subprocess
from agent.utils.tool_logger import log_tool


def run_kubectl_command(command):

    try:

        # Log command start
        log_tool(f"Running kubectl command: {' '.join(command)}")

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        # Log completion
        log_tool(
            f"Completed kubectl command: {' '.join(command)}"
        )

        return result.stdout

    except Exception as e:

        log_tool(
            f"Error running command {' '.join(command)}: {str(e)}"
        )

        return str(e)


def process_query(query):

    # Log user query
    log_tool(f"User Query Received: {query}")

    query = query.lower()

    # --------------------------------
    # Pod Status
    # --------------------------------

    if "pod" in query and "status" in query:

        log_tool("Processing: Pod Status Query")

        output = run_kubectl_command(
            ["kubectl", "get", "pods"]
        )

        return f"📋 Pod Status:\n\n{output}"

    # --------------------------------
    # Failing Pods (IMPROVED VERSION)
    # --------------------------------

    elif "failing" in query or "crash" in query:

        log_tool("Processing: Failing Pods Query")

        output = run_kubectl_command(
            ["kubectl", "get", "pods"]
        )

        lines = output.split("\n")

        failing = []

        for line in lines[1:]:

            if line.strip() == "":
                continue

            parts = line.split()

            pod_name = parts[0]
            status = parts[2]

            # Detect non-running pods
            if status != "Running":

                failing.append(
                    f"⚠️ {pod_name} → {status}"
                )

        if not failing:

            return "✅ No failing pods detected."

        return "\n".join(failing)

    # --------------------------------
    # Logs
    # --------------------------------

    elif "logs" in query:

        log_tool("Processing: Logs Query")

        words = query.split()

        for word in words:

            if "pod" in word:

                pod_name = word

                logs = run_kubectl_command(
                    ["kubectl", "logs", pod_name, "--all-namespaces"]
                )

                return f"📄 Logs for {pod_name}:\n\n{logs}"

        return "⚠️ Please specify pod name."

    # --------------------------------
    # Memory Usage
    # --------------------------------

    elif "memory" in query:

        log_tool("Processing: Memory Usage Query")

        output = run_kubectl_command(
            ["kubectl", "top", "pods"]
        )

        return f"📊 Memory Usage:\n\n{output}"

    # --------------------------------
    # Default Help
    # --------------------------------

    else:

        log_tool("Processing: Default Help Query")

        return (
            "🤖 I can help with:\n"
            "- pod status\n"
            "- failing pods\n"
            "- logs pod <pod-name>\n"
            "- memory usage\n"
        )