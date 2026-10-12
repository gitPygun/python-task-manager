import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n--- Your Tasks ---")

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['title']}")


def add_task(tasks):
    """Add a new task."""
    title = input("\nEnter a task: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def complete_task(tasks):
    """Mark a task as completed."""
    show_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter the task number to complete: "))

        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    """Delete a task."""
    show_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter the task number to delete: "))

        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Deleted: {deleted_task['title']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    """Main program."""
    tasks = load_tasks()

    while True:
        print("\n====================")
        print("     TASK MANAGER")
        print("====================")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()