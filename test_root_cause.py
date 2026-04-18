from agent.reasoning.root_cause_engine import get_root_cause


def test_root_cause():
    result = get_root_cause()
    print(result)


if __name__ == "__main__":
    test_root_cause()