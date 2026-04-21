from agent.reasoning.root_cause_engine import get_root_cause
from agent.reasoning.recommendation_engine import generate_recommendations
from agent.reasoning.health_summary import get_cluster_summary
from agent.prompts.diagnosis_prompt import build_diagnosis_prompt
from agent.prompts.recommendation_prompt import build_recommendation_prompt


def run_agent():

    print("\n🔍 Checking Kubernetes Cluster...\n")

    # Get summary
    summary = get_cluster_summary()

    print("📊 Cluster Health Summary:\n")

    print(f"Total Pods: {summary['total']}")
    print(f"Running Pods: {summary['running']}")
    print(f"Failing Pods: {summary['failing']}")

    print("\n⚠️ Issues Detected:\n")

    issues = get_root_cause()

    # Build AI prompts (future LLM use)

    diagnosis_prompt = build_diagnosis_prompt(issues)

    recommendation_prompt = build_recommendation_prompt(issues)

    # Optional debug output
    #print("\n🧠 Diagnosis Prompt:\n")
    #print(diagnosis_prompt)

    for issue in issues:
        print(issue)

    recommendations = generate_recommendations(issues)

    if recommendations:

        print("\n📌 Suggested Fixes:\n")

        for rec in recommendations:
            print(rec)


if __name__ == "__main__":
    run_agent()
