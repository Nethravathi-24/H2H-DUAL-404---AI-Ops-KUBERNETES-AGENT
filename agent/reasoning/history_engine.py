import json
import os
from datetime import datetime

# Safe absolute path to data folder
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")
)

DATA_DIR = os.path.join(BASE_DIR, "data")

HISTORY_FILE = os.path.join(
    DATA_DIR,
    "history.json"
)

# Ensure folder exists
os.makedirs(DATA_DIR, exist_ok=True)


def load_history():

    if not os.path.exists(HISTORY_FILE):

        return []

    with open(HISTORY_FILE, "r") as f:

        try:
            return json.load(f)
        except:
            return []


def save_history(history):

    with open(HISTORY_FILE, "w") as f:

        json.dump(history, f, indent=4)


def log_issues(issues):

    history = load_history()

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    for issue in issues:

        entry = {
            "time": timestamp,
            "issue": issue
        }

        history.append(entry)

    save_history(history)


def get_recent_history(limit=10):

    history = load_history()

    return history[-limit:]