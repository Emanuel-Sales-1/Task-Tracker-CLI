import json
from datetime import datetime

while True:
    command = input().lower()

    match command:
        case "help":
            print(
                "=" * 82,
                "\nAll commands:\n",
                "add    [task_title] (task_description) - adds a task\n",
                "list   [class]                         - list tasks\n",
                "update [class] [new_title] [id]        - updates a task\n",
                "delete [id]                            - delete a task\n",
                "mark   [new_status] [id]               - marks a task as done, todo or in progess\n",
                "exit                                   - closes the program\n"+
                ("=" * 82)
                )
        case "add":
            pass
        case "list":
            pass
        case "update":
            pass
        case "delete":
            pass
        case "mark":
            pass
        case "exit":
            break
        case _:
            print("invalid input. Try again...\n")
  