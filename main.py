from agent.reasoning.root_cause_engine import get_root_cause
from agent.reasoning.health_summary import get_cluster_summary
from agent.nl_query_engine import process_query
from agent.utils.tool_logger import log_tool
from agent.agent_core import start_ai_assistant
from agent.reasoning.root_cause_engine import get_root_cause

def show_cluster_health():

    print("\n🔍 Checking Cluster Health...\n")

    summary = get_cluster_summary()

    print("📊 Cluster Summary")
    print("-------------------")
    print(f"Total Pods   : {summary['total']}")
    print(f"Running Pods : {summary['running']}")
    print(f"Failing Pods : {summary['failing']}")


def show_root_cause():

    print("\n🧠 Running Root Cause Analysis...\n")

    issues = get_root_cause()

    print("🚨 Detected Issues")
    print("-------------------")

    for issue in issues:
        print(issue)


def start_query_loop():

    print("\n🤖 AI Ops Assistant Ready!")
    print("Type 'exit' to quit.\n")

    while True:

        query = input("Ask AI Ops > ")

        if query.lower() == "exit":
            print("👋 Exiting AI Ops Assistant...")
            break

        response = process_query(query)

        print("\n", response, "\n")


def main():

    log_tool("AI Ops Agent Started")

    print("\n🚀 AI Ops Kubernetes Agent Starting...\n")

    # Step 1: Show cluster health
    show_cluster_health()

    # Step 2: Run root cause analysis
    show_root_cause()

    # Step 3: Start AI query interface
    start_query_loop()

    log_tool("AI Ops Agent Stopped")


if __name__ == "__main__":
    main()
