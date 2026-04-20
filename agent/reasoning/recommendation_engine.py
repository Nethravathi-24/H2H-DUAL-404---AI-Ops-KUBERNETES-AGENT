def generate_recommendations(issues):
    """
    Generate recommendations based on detected issues.
    """

    recommendations = []

    for issue in issues:

        issue_lower = issue.lower()

        # CrashLoop recommendations
        if "crashing" in issue_lower:

            recommendations.append(
                "💡 Recommendation: Check container logs and image configuration."
            )

        # Memory recommendations
        elif "high memory" in issue_lower:

            recommendations.append(
                "💡 Recommendation: Increase memory limits or optimize memory usage."
            )

        # CPU recommendations
        elif "high cpu" in issue_lower:

            recommendations.append(
                "💡 Recommendation: Optimize CPU usage or scale replicas."
            )

    return recommendations