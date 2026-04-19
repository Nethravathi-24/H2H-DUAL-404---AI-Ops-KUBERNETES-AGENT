from agent.tools.kubectl_tool import get_pods
from agent.tools.log_tool import get_pod_logs
from agent.memory.memory_manager import log_event


def analyze_pod_status():
    """
    Analyze pod status and detect failures
    """

    pods = get_pods()

    issues = []

    for pod in pods:

        name = pod["name"]
        status = pod["status"]

        if status == "CrashLoopBackOff":
            issues.append(
                f"Pod {name} crashing repeatedly"
            )

        elif status == "Pending":
            issues.append(
                f"Pod {name} stuck in Pending"
            )

        elif status == "Error":
            issues.append(
                f"Pod {name} has error state"
            )

    # Save issues to memory
    if issues:
        for issue in issues:
            log_event(issue)

    return issues


def get_root_cause():
    """
    Determine root cause using logs
    """

    pods = get_pods()

    if not pods:
        return ["No pods found."]

    causes = []

    for pod in pods:

        name = pod["name"]
        status = pod["status"]

        if status == "CrashLoopBackOff":

            logs = get_pod_logs(name)

            if "connection refused" in logs.lower():
                causes.append(
                    f"Pod {name} crashing — service connection refused."
                )

            elif "no module named" in logs.lower():
                causes.append(
                    f"Pod {name} crashing — Python dependency missing."
                )

            else:
                causes.append(
                    f"Pod {name} crashing repeatedly — check logs."
                )

        elif status == "Pending":
            causes.append(
                f"Pod {name} stuck in Pending — check resources."
            )

        elif status == "Error":
            causes.append(
                f"Pod {name} has error state."
            )

    if not causes:
        return ["No issues detected. Cluster healthy."]

    return causes
