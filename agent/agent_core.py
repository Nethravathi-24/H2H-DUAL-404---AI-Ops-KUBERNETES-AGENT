from agent.reasoning.root_cause_engine import get_root_cause


def run_agent():
    print("\n🔍 Checking Kubernetes Cluster...\n")

    results = get_root_cause()

    if isinstance(results, str):
        print(results)

    else:
        for result in results:
            print("⚠️", result)


if __name__ == "__main__":
    run_agent()
