import sys, argparse, json
from datetime import datetime, timezone
from pathlib import Path

TASKS_FILE = Path.cwd() / "tasks.json"
VALID_STATUSES = ("todo", "in-progress", "done")

def main():
    ensure_file_exists()

# Returns current time in ISO 8601 format
def now_iso():
    return datetime.now(timezone.utc).astimezone().isoformat()

def ensure_file_exists():
    # If tasks.json file doesn't exist, create a tasks.json file with an empty list in it
    if not TASKS_FILE.exists():
        try:
            with open(TASKS_FILE, "w") as file:
                json.dump([], file, indent=2)
        except Exception as e:
            print(f"Failed to create tasks file: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()