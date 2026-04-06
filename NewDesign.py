import json
from datetime import datetime
from pathlib import Path

script_dir = Path(__file__).parent

def Get_Last_ID():
    while True:
        try:
            with open(script_dir/"data/IdCount.txt", "r+") as f:
                lastId = f.read()
                currentId = int(lastId) + 1
            with open(script_dir/"data/IdCount.txt", "w") as f:
                f.write(str(currentId))
                break
        except FileNotFoundError:
            with open(script_dir/"data/IdCount.txt", "w") as f:
                f.write("0")
    return currentId

def Help(command):
    try:
        match command[1]:
            case "add":
                print("add [task_title] (task_description) - adds a task")
            case "list":
                print("list [class] - list tasks")
            case "update":
                print("update [class] [new_title] [id] - updates a task")
            case "delete":
                print("delete [id] - delete a task")
            case "mark":
                print("mark [new_status] [id] - marks a task as done, todo or in progess")
            case "exit":
                print("exit - closes the program")
            case _:
                print("invalid input. Try again...\n")
    except IndexError:
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
def Add_Task(command):
    try:
        description = command[2]
    except:
        description = "Description empty"
    try:
        currentId = Get_Last_ID()
        currentTask = {
            "id": currentId,
            "title": command[1],
            "description": description,
            "stauts": "todo",
            "createdAt": datetime.now().strftime("%Y-%m-%d %I:%M %p"),
            "lastUpdateAt": datetime.now().strftime("%Y-%m-%d %I:%M %p")
        }
        with open(script_dir/"data/TaskList.json", "a+") as f:
            json.dump(currentTask, f, indent= 4)
        print(f"Task added successfully! (Id {currentId})")
    except IndexError:
        print("Invalid input. Try again...")

while True:
    command = input("-> ").lower().split()
    try:
        mainCommand = command[0]
    except IndexError:
        mainCommand = "Invalid input"

    match mainCommand:
        case "help":
            Help(command)
        case "add":
            Add_Task(command)
        case "list":
            try:
                command[1]
            except IndexError:
                print("Invalid input. Try again...")
        case "update":
            try:
                command[1]
            except IndexError:
                print("Invalid input. Try again...")
        case "delete":
            try:
                command[1]
            except IndexError:
                print("Invalid input. Try again...")
        case "mark":
            try:
                command[1]
            except IndexError:
                print("Invalid input. Try again...")
        case "exit":
            break
        case _:
            print("invalid input. Try again...")
  