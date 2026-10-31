
import json


# Function to load tasks from JSON file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# Function to save tasks in JSON file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


# Function to add a new task
def add_task():
    title = input("Enter task title: ").strip()

    if title == "":
        print("Error: Task title cannot be empty!")
        return

    tasks.append({
        "title": title,
        "done": False
    })

    save_tasks()
    print("Task added successfully!")


# Function to view all tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available!")
        return

    print("\n--- YOUR TASKS ---")

    for index, task in enumerate(tasks, start=1):

        if task["done"] == True:
            status = "Done"
        else:
            status = "Pending"

        print(f"{index}. {task['title']} [{status}]")


# Function to complete a task
def complete_task():
    if len(tasks) == 0:
        print("No tasks available to complete!")
        return

    view_tasks()

    try:
        number = int(input("Enter task number to complete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number!")
            return

        tasks[number - 1]["done"] = True

        save_tasks()
        print("Task completed successfully!")

    except ValueError:
        print("Please enter a valid number!")


# Function to delete a task
def delete_task():
    if len(tasks) == 0:
        print("No tasks available to delete!")
        return

    view_tasks()

    try:
        number = int(input("Enter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number!")
            return

        removed_task = tasks.pop(number - 1)

        save_tasks()
        print(f"Task '{removed_task['title']}' deleted successfully!")

    except ValueError:
        print("Please enter a valid number!")


# Load existing tasks when program starts
tasks = load_tasks()


# Main menu
while True:

    print("\n========== TASK TRACKER ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Thank you for using Task Tracker!")
        break

    else:
        print("Invalid choice! Please select between 1 and 5.")
