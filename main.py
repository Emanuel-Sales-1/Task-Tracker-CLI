import json
from datetime import datetime

tasksList = []

def Get_Last_ID():
    while True:
        try:
            with open("Python Challenges/Task Tracker CLI/IdCount.txt", "r+") as f:
                lastId = f.read()
                currentId = int(lastId) + 1
            with open("Python Challenges/Task Tracker CLI/IdCount.txt", "w") as f:
                f.write(str(currentId))
                break
        except FileNotFoundError:
            with open("Python Challenges/Task Tracker CLI/IdCount.txt", "w") as f:
                f.write("0")

    return currentId

def Show_Menu():
    print("--- Task Tracker ---")
    print("1. List tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Close")
    print("--------------------")
    return input("Chose a option: ")

def List_Tasks():
    print("1. All tasks")
    print("2. Todo tasks")
    print("3. In progress tasks")
    print("4. Finished tasks")
    
    

def Add_Task():
    currentId = Get_Last_ID()
    currentTask = {
        "id": currentId,
        "title": str(input("Title: ")),
        "description": str(input("Description: ")),
        "stauts": "todo",
        "createdAt": datetime.now().strftime("%Y-%m-%d %I:%M %p"),
        "lastUpdateAt": datetime.now().strftime("%Y-%m-%d %I:%M %p")
    }
    with open("Python Challenges/Task Tracker CLI/TaskList.json", "a+") as f:
        json.dump(currentTask, f, indent= 4)
    print(f"Task added successfully! (Id {currentId})")
    
while True:
    
    try:
        option = int(Show_Menu())
    except ValueError:
        print("Invalid input. Try again...")
        input()
        option = 6
        
    match option:
        case 1:
            pass
        case 2:
            Add_Task()
        case 3:
            pass
        case 4:
            pass
        case 5:
            break
        case 6:
            pass
        case _:
            print("Invalid input. Try again...")
            input()