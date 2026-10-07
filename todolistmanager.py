# Project 3 - To-Do List Manager
import json, os
FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            try: return json.load(f)
            except: return []
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)

tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter task: ")
        tasks.append({"task": task_name, "done": False})
        save_tasks(tasks)
        print("Task added!")
    elif choice == "2":
        if not tasks: print("No tasks yet.")
        else:
            for i, t in enumerate(tasks):
                status = "Done" if t["done"] else "Pending"
                print(f"{i+1}. {t['task']} - [{status}]")
    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        save_tasks(tasks)
        print("Task deleted")
    elif choice == "4":
        num = int(input("Enter task number to mark as done: "))
        tasks[num-1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!")
    elif choice == "5":
        print("Goodbye!")
        break