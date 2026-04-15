import json
from datetime import datetime
from pathlib import Path
import shlex

# find the script path
script_dir = Path(__file__).parent
taskList = {"Tasks":[]}
def ReadFile():
    with open(script_dir/"data/TaskList.json", "r") as f:
        if f.read().strip():
            f.seek(0)
            newFile = json.load(f)
    return newFile

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
            "list   [Filter]                        - list tasks\n",
            "update [class] [new_title] [id]        - updates a task\n",
            "delete [id]                            - delete a task\n",
            "mark   [new_status] [id]               - marks a task as done, todo or in progess\n",
            "exit                                   - closes the program\n"+
            ("=" * 82)
            )
        
def List_Tasks(option):
        with open(script_dir/"data/TaskList.json", "r") as f:
            taskList = json.load(f)
        if len(option) == 1:
            for i in taskList["Tasks"]:
                print(
                    "="*50,"\n",
                    "Title:",i["title"],"\n",
                    "Description:",i["description"],"\n",
                    "Status:", i["status"],"\n"
                    " Created at:", i["createdAt"],"\n"
                    " Last updated at:", i["lastUpdatedAt"],"\n",
                    "ID:",i["id"],
                    )
        elif len(option) == 2 and option[1] in ["todo", "done", "in-progress"]:
            for i in taskList["Tasks"]:
                if i["status"] == option[1]:
                    print(
                        "="*50,"\n",
                        "Title:",i["title"],"\n",
                        "Description:",i["description"],"\n",
                        "Status:", i["status"],"\n"
                        " Created at:", i["createdAt"],"\n"
                        " Last updated at:", i["lastUpdatedAt"],"\n",
                        "ID:",i["id"],
                        )
        else:
            print("Invalid input. Try again...")
        

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
            "status": "todo",
            "createdAt": datetime.now().strftime("%Y-%m-%d %I:%M %p"),
            "lastUpdatedAt": datetime.now().strftime("%Y-%m-%d %I:%M %p")
        }

        try:
            with open(script_dir/"data/TaskList.json", "r") as f:
                if f.read().strip():
                    f.seek(0)
                    taskList = json.load(f)
            with open(script_dir/"data/TaskList.json", "w+") as f:
                taskList["Tasks"].append(currentTask)
                json.dump(taskList,f, indent=2)
        except FileNotFoundError:
            print("File Not Found Error")
        print(f"Task added successfully! (Id {currentId})")
    except IndexError:
        print("Invalid input. Try again...")

def Delete_task(option):
    taskList = ReadFile()
    if len(option) == 2:
        taskList["Tasks"] = [i for i in taskList["Tasks"] if i["id"] != int(option[1])]
    else:
        print("Invalid input. Try again...")
    with open(script_dir/"data/TaskList.json", "w+") as f:
        json.dump(taskList, f, indent=2)


while True:
    commandInputs = input("-> ").lower()
    
    try:
        command = shlex.split(commandInputs, posix=False)
        mainCommand = command[0]
    except ValueError:
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
            Delete_task(command)
        case "mark":
            try:
                command[1]
            except IndexError:
                print("Invalid input. Try again...")
        case "exit":
            break
        case _:
            print("invalid input. Try again...")
  