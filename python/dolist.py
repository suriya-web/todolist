import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load existing tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    task = input("Enter task description: ")
    tasks.append({"id": len(tasks) + 1, "task": task, "completed": False})
    save_tasks(tasks)
    print("✅ Task added successfully!")

# View all tasks
def view_tasks():
    if not tasks:
        print("📭 No tasks found!")
        return
    print("\n📌 To-Do List:")
    for task in tasks:
        status = "✔" if task["completed"] else "❌"
        print(f"{task['id']}. {task['task']} [{status}]")

# Update a task
def update_task():
    view_tasks()
    task_id = int(input("\nEnter Task ID to update: "))
    for task in tasks:
        if task["id"] == task_id:
            new_task = input("Enter new description: ")
            task["task"] = new_task
            save_tasks(tasks)
            print("✅ Task updated successfully!")
            return
    print("⚠ Task ID not found!")

# Delete a task
def delete_task():
    view_tasks()
    task_id = int(input("\nEnter Task ID to delete: "))
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("🗑 Task deleted successfully!")

# Mark a task as completed
def complete_task():
    view_tasks()
    task_id = int(input("\nEnter Task ID to mark as completed: "))
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("🎉 Task marked as completed!")
            return
    print("⚠ Task ID not found!")

# Main menu
tasks = load_tasks()

while True:
    print("\n📋 To-Do List Menu:")
    print("1️⃣ Add Task")
    print("2️⃣ View Tasks")
    print("3️⃣ Update Task")
    print("4️⃣ Delete Task")
    print("5️⃣ Mark Task as Completed")
    print("0️⃣ Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        complete_task()
    elif choice == "0":
        print("👋 Exiting To-Do List. Have a productive day!")
        break
    else:
        print("❌ Invalid choice! Please select a valid option.")
