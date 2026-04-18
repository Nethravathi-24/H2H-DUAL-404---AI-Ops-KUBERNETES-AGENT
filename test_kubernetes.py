from agent.tools.kubectl_tool import get_pods


def test_get_pods():
    pods = get_pods()
    print(pods)


if __name__ == "__main__":
    test_get_pods()