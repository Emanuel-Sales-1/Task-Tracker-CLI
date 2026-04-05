
tasksList = []

def showMenu():
    print("--- Task Tracker ---")
    print("1. List tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Close")
    print("--------------------")
    return int(input("Chose a option: "))



while True:

    option = showMenu()
    print(option==int)
    
    match option:
        case 1:
            print(1)
        case 2:
            print(12)
        case 3:
            pass
        case 4:
            pass
        case 5:
            break
        case _:
            print("Invalid input. Try again...")
            input()