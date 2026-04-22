import subprocess
from agent.tools.log_tool import get_pod_logs
from agent.utils.tool_logger import log_tool


def analyze_pod_status():
    """
    Detect pod failures and analyze logs
    to identify possible root causes.
    """

    try:

        log_tool("Running: kubectl get pods")

        result = subprocess.run(
            ["kubectl", "get", "pods"],
            capture_output=True,
            text=True
        )

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

            # Detect failing pods
            if status in ["Error", "CrashLoopBackOff"]:

                log_tool(
                    f"Failure detected in pod: {pod_name}"
                )

                logs = get_pod_logs(pod_name)

                if logs:

                    logs_lower = logs.lower()

                    # Smart root cause detection
                    if "connection refused" in logs_lower:

                        issue = (
                            f"⚠️ Pod {pod_name} failing — "
                            f"backend service not reachable"
                        )

                    elif "crashloopbackoff" in logs_lower:

                        issue = (
                            f"⚠️ Pod {pod_name} failing — "
                            f"CrashLoopBackOff detected"
                        )

                    elif "imagepull" in logs_lower:

                        issue = (
                            f"⚠️ Pod {pod_name} failing — "
                            f"image pull error"
                        )

                    elif "not found" in logs_lower:

                        issue = (
                            f"⚠️ Pod {pod_name} failing — "
                            f"missing resource"
                        )

                    elif "error" in logs_lower:

                        issue = (
                            f"⚠️ Pod {pod_name} failing — "
                            f"application error detected"
                        )

                    else:

                        issue = (
                            f"⚠️ Pod {pod_name} failing — "
                            f"startup error suspected"
                        )

                else:

                    issue = (
                        f"⚠️ Pod {pod_name} failing — "
                        f"logs unavailable."
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
    """

    try:

        log_tool("Running: kubectl top pods")

        result = subprocess.run(
            ["kubectl", "top", "pods"],
            capture_output=True,
            text=True
        )

        log_tool("Completed: kubectl top pods")

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
            cpu = parts[1]
            memory = parts[2]

            # Memory Analysis
            if "Mi" in memory:

                try:
                    mem_value = int(
                        memory.replace("Mi", "")
                    )

                    if mem_value > 300:

                        issue = (
                            f"⚠️ Pod {pod_name} "
                            f"using high memory ({memory})"
                        )

                        issues.append(issue)
                        log_tool(issue)

                except:
                    continue

            # CPU Analysis
            if "m" in cpu:

                try:
                    cpu_value = int(
                        cpu.replace("m", "")
                    )

                    if cpu_value > 500:

                        issue = (
                            f"⚠️ Pod {pod_name} "
                            f"using high CPU ({cpu})"
                        )

                        issues.append(issue)
                        log_tool(issue)

                except:
                    continue

        return issues

    except Exception as e:

        log_tool(
            f"Error in analyze_pod_metrics: {str(e)}"
        )

        return [str(e)]


def get_root_cause():
    """
    Combine all diagnostics into
    one unified root cause output.
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
