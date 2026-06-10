import json


# Load tasks from JSON file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


# Save tasks to JSON file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


# Add new task
def add_task():
    tasks = load_tasks()

    task_name = input("\nEnter task: ").strip()

    if not task_name:
        print("Task cannot be empty.")
        return

    tasks.append({
        "task": task_name,
        "completed": False
    })

    save_tasks(tasks)

    print("Task added successfully!")


# View all tasks
def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n===== TASK LIST =====")

    for index, task in enumerate(tasks, start=1):

        status = "✓" if task["completed"] else "✗"

        print(f"{index}. [{status}] {task['task']}")


# Delete task
def delete_task():
    tasks = load_tasks()

    if not tasks:
        print("\nNo tasks available to delete.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):

            removed_task = tasks.pop(task_number - 1)

            save_tasks(tasks)

            print(f"Task '{removed_task['task']}' deleted successfully!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Mark task as completed
def mark_completed():
    tasks = load_tasks()

    if not tasks:
        print("\nNo tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("\nEnter task number to mark as completed: "))

        if 1 <= task_number <= len(tasks):

            tasks[task_number - 1]["completed"] = True

            save_tasks(tasks)

            print("Task marked as completed!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Main menu
def main():

    while True:

        print("\n==============================")
        print("      TO-DO LIST MENU")
        print("==============================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task Completed")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            mark_completed()

        elif choice == "5":
            print("\nThank you for using the To-Do List Application!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start Program
main()