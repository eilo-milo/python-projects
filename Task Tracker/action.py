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


def list_task(status_filter=None):
    tasks=load_tasks()
    if not tasks:
        print ("no tasks found")
        return
    filtered= tasks
    if status_filter:
        filtered=[t for t in tasks if ["status"]== status_filter]
        return
    for t in filtered:
        print(f"[{t['id']}] {t['description']} | Status: {t['status']} | Updated: {t['updatedAt']} ")

    


def update (task_id, new_description):
    tasks =load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["description"] = new_description
            t["updatedAt"] = datetime.now().isoformat()
            save_taks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Error: Task ID {task_id} not found.")  



def delete (task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len (tasks)== len ( new_tasks):
      print(f"Error: Task ID {task_id} not found.")
    else:
        save_taks(new_tasks)
        print(f"Task {task_id} deleted successfully.")  


def mark_status(task_id, status):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = status
            t["updatedAt"] = datetime.now().isoformat()
            save_taks(tasks)
            print(f"Task {task_id} marked as '{status}'.")
            return
    print(f"Error: Task ID {task_id} not found.")