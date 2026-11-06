from storage import load_tasks
from storage import save_taks
from datetime import datetime
def add (description):
    tasks= load_tasks()
    # generate a new id by getting the max id and adding 1 on it 
    new_id  = max([t["id"] for t in tasks], default=0)+1
    now = datetime.now().isoformat()
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(new_task)
    save_taks(tasks)
    print(f"Task added successfully (ID: {new_id})")


def list_task():
    pass


def update ():
    pass


def delete ():
    pass

def mark_status():
    pass