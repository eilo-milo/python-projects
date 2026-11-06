import sys
import os
import json
DB_FILE = "tasks.json"
def load_tasks():
 """Load tasks from tasks.json file. If file doesn't exist, return empty list."""
 if not os.path.exists(DB_FILE):
        return []
 try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
 except json.JSONDecodeError:
        return []

def save_taks(tasks):
 """Save the list of tasks back to tasks.json."""
 with open (DB_FILE,"w") as f:
      json.dump(tasks,f, indent=4)