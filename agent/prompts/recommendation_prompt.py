def build_recommendation_prompt(issues):
    """
    Build structured recommendation prompt
    from detected issues.
    """

    base_prompt = """
You are an expert Kubernetes SRE.

Based on the detected issues below,
suggest practical fixes.

Cluster Issues:
"""

    for issue in issues:
        base_prompt += f"- {issue}\n"

    base_prompt += """

Provide:
1. Immediate Fix
2. Long-term Prevention
3. Best Kubernetes Practice

Return recommendations in bullet points.
"""

    return base_prompt