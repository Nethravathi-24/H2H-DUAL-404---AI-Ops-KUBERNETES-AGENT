import os
from datetime import datetime

LOG_FILE = "logs/agent_logs.txt"


def log_event(event):
    """
    Store event logs with timestamp
    """
    try:
        os.makedirs("logs", exist_ok=True)

        with open(LOG_FILE, "a") as f:
            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            f.write(f"[{timestamp}] {event}\n")

    except Exception as e:
        print(f"Logging error: {e}")


def read_logs():
    """
    Read stored logs
    """
    try:
        if not os.path.exists(LOG_FILE):
            return "No logs available."

        with open(LOG_FILE, "r") as f:
            return f.read()

    except Exception as e:
        return str(e)
