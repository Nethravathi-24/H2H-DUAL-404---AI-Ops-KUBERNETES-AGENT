from agent.tools.kubectl_tool import get_pods
from agent.tools.log_tool import get_pod_logs
from agent.memory.memory_manager import log_event


def analyze_pods():
    """
    Analyze pod status and detect failures
    """
    pods_output = get_pods()

    issues = []

    # Detect common failure states
    if "CrashLoopBackOff" in pods_output:
        issues.append("CrashLoopBackOff detected")

    if "ImagePullBackOff" in pods_output:
        issues.append("ImagePullBackOff detected")

    if "Pending" in pods_output:
        issues.append("Pending pod detected")

    if "Error" in pods_output:
        issues.append("Pod error detected")

    # Log detected issues
    if issues:
        for issue in issues:
            log_event(f"Issue detected: {issue}")

    return issues


def get_root_cause():
    """
    Determine root cause of issues
    """
    issues = analyze_pods()

    if not issues:
        return "No issues detected. Cluster healthy."

    causes = []

    for issue in issues:

        if "CrashLoopBackOff" in issue:
            causes.append(
                "Pod crashing repeatedly — check container logs."
            )

        elif "ImagePullBackOff" in issue:
            causes.append(
                "Image not found — check container image name."
            )

        elif "Pending" in issue:
            causes.append(
                "Insufficient resources — check CPU/Memory."
            )

        elif "Error" in issue:
            causes.append(
                "Pod error detected — inspect logs."
            )

    return causes
