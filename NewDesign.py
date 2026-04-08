import json
from datetime import datetime
from pathlib import Path
import shlex

# find the script path
script_dir = Path(__file__).parent

def Get_List():
    pass

def Get_Last_ID():
    # Create a IdCount file to track the current id, if the file don't exist it creates
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

def Help(option):
    # Help command to get a list of the possible commands
    try:
        match option[1]:
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
        # Specific search
        print(
            "=" * 82,
            "\nAll commands:\n",
            "add    [task_title] (task_description) - adds a task\n",
            "list   [Filter]                         - list tasks\n",
            "update [class] [new_title] [id]        - updates a task\n",
            "delete [id]                            - delete a task\n",
            "mark   [new_status] [id]               - marks a task as done, todo or in progess\n",
            "exit                                   - closes the program\n"+
            ("=" * 82)
            )
        
def List_Tasks(option):
        with open(script_dir/"data/TaskList.json", "r") as f:
            taskList = json.load(f)
        print(taskList)
        

def Add_Task(option):
    # Detects if the user passed a description
    try:
        description = option[2]
    except IndexError:
        description = "Description empty"

    try:
        currentId = Get_Last_ID()
        currentTask = {
            "id": currentId,
            "title": option[1],
            "description": description,
            "stauts": "todo",
            "createdAt": datetime.now().strftime("%Y-%m-%d %I:%M %p"),
            "lastUpdateAt": datetime.now().strftime("%Y-%m-%d %I:%M %p")
        }
        
        TaskList = {"Tasks": [currentTask]}

        with open(script_dir/"data/TaskList.json", "w") as f:
            json.dump(TaskList, f, indent= 2)
        print(f"Task added successfully! (Id {currentId})")
    except IndexError:
        print("Invalid input. Try again...")

while True:
    commandInputs = input("-> ").lower()
    command = shlex.split(commandInputs, posix=False)
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
            List_Tasks(command)
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
  