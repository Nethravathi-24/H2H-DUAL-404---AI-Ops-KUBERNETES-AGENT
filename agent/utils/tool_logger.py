import datetime
import os

LOG_FILE = "tool_logs.txt"


def log_tool(message):

    try:

        timestamp = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        log_entry = f"[{timestamp}] {message}\n"

        with open(LOG_FILE, "a") as f:
            f.write(log_entry)

    except Exception:

        pass
