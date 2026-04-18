from agent.memory.memory_manager import log_event, read_logs


def test_memory():
    log_event("Test event: Kubernetes agent started")
    logs = read_logs()
    print(logs)


if __name__ == "__main__":
    test_memory()