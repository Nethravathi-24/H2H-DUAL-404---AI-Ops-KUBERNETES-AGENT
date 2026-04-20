import subprocess
from agent.tools.log_tool import get_pod_logs
from agent.utils.tool_logger import log_tool


def analyze_pod_status():
    """
    Detect pod failures like CrashLoopBackOff
    and analyze logs for deeper root cause.
    """

    try:

        # LOG kubectl command
        log_tool("Running: kubectl get pods")

        result = subprocess.run(
            ["kubectl", "get", "pods"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
    
            error_msg = (
                "⚠️ Unable to fetch pod status. "
                "Check Kubernetes cluster connection."
            )

            log_tool(error_msg)

            return [error_msg]

        log_tool("Completed: kubectl get pods")

        output = result.stdout
        lines = output.split("\n")

        issues = []

        for line in lines[1:]:

            if line.strip() == "":
                continue

            parts = line.split()

            # Safety check
            if len(parts) < 3:
                continue

            pod_name = parts[0]
            status = parts[2]

            # Detect crashing pods
            if "CrashLoopBackOff" in status:

                log_tool(
                    f"CrashLoop detected in pod: {pod_name}"
                )

                logs = get_pod_logs(pod_name)

                if logs:

                    logs_lower = logs.lower()

                    if "connection refused" in logs_lower:

                        issue = (
                            f"⚠️ Pod {pod_name} crashing — connection refused detected"
                        )

                    elif "error" in logs_lower:

                        issue = (
                            f"⚠️ Pod {pod_name} crashing — error found in logs"
                        )

                    elif "not found" in logs_lower:

                        issue = (
                            f"⚠️ Pod {pod_name} crashing — resource not found"
                        )

                    else:

                        issue = (
                            f"⚠️ Pod {pod_name} crashing repeatedly — check logs."
                        )

                else:

                    issue = (
                        f"⚠️ Pod {pod_name} crashing repeatedly — logs unavailable."
                    )

                issues.append(issue)
                log_tool(issue)

        return issues

    except Exception as e:

        log_tool(
            f"Error in analyze_pod_status: {str(e)}"
        )

        return [str(e)]


def analyze_pod_metrics():
    """
    Detect high memory and CPU usage.
    FIXED version — safe parsing for --all-namespaces output.
    """

    try:

        # LOG kubectl top command
        log_tool("Running: kubectl top pods")

        result = subprocess.run(
            ["kubectl", "top", "pods", "--all-namespaces"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
    
            error_msg = (
                "⚠️ Unable to fetch pod metrics. "
                "Metrics server may not be installed."
            )

            log_tool(error_msg)

            return [error_msg]

        log_tool("Completed: kubectl top pods")

        output = result.stdout
        lines = output.split("\n")

        issues = []

        for line in lines[1:]:

            if line.strip() == "":
                continue

            parts = line.split()

            # Expected format:
            # NAMESPACE NAME CPU MEMORY

            if len(parts) < 4:
                continue

            namespace = parts[0]
            pod_name = parts[1]
            cpu = parts[2]
            memory = parts[3]

            # --------------------
            # MEMORY CHECK
            # --------------------

            if "Mi" in memory:

                try:
                    mem_value = int(
                        memory.replace("Mi", "")
                    )
                except:
                    mem_value = 0

                if mem_value > 300:

                    issue = (
                        f"⚠️ Pod {pod_name} using high memory ({memory})"
                    )

                    issues.append(issue)
                    log_tool(issue)

            # --------------------
            # CPU CHECK
            # --------------------

            if "m" in cpu:

                try:
                    cpu_value = int(
                        cpu.replace("m", "")
                    )
                except:
                    cpu_value = 0

                if cpu_value > 500:

                    issue = (
                        f"⚠️ Pod {pod_name} using high CPU ({cpu})"
                    )

                    issues.append(issue)
                    log_tool(issue)

        return issues

    except Exception as e:

        log_tool(
            f"Error in analyze_pod_metrics: {str(e)}"
        )

        return [str(e)]


def get_root_cause():
    """
    Combine all diagnostics.
    Final unified root cause output.
    """

    log_tool("Starting root cause analysis")

    pod_issues = analyze_pod_status()

    metric_issues = analyze_pod_metrics()

    all_issues = pod_issues + metric_issues

    if not all_issues:

        log_tool("Cluster healthy")

        return ["✅ Cluster healthy"]

    log_tool(
        f"Total issues detected: {len(all_issues)}"
    )

    return all_issues