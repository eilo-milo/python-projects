import sys
from action import add
from action import delete 
from action import mark_status
from action import list_task


def main():
    if len(sys.argv) < 2:
        print("Usage: python task.py <command> [arguments]")
        return

    command = sys.argv[1].lower()
    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Missing task description.")
            return
        add(sys.argv[2])

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python task.py delete <id>")
            return
        delete(int(sys.argv[2]))

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: python task.py mark-in-progress <id>")
            return
        mark_status(int(sys.argv[2]), "in-progress")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: python task.py mark-done <id>")
            return
        mark_status(int(sys.argv[2]), "done")

    elif command == "list":
        status_filter = sys.argv[2] if len(sys.argv) > 2 else None
        list_task(status_filter)

    else:
        print(f"Unknown command: '{command}'")  



main ()    