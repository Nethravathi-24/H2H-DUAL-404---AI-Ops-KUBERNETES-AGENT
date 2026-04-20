def build_diagnosis_prompt(issues):
    """
    Build a structured diagnosis prompt
    based on detected cluster issues.
    """

    base_prompt = """
You are an AI Kubernetes troubleshooting assistant.

Analyze the following detected issues
and provide a clear root cause explanation.

Cluster Issues:
"""

    for issue in issues:
        base_prompt += f"- {issue}\n"

    base_prompt += """

Explain:
1. What caused these issues
2. Which service or pod is affected
3. What could be the underlying reason

Provide output in clear bullet points.
"""

    return base_prompt