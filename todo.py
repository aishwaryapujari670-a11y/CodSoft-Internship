# TASK 1 - TO-DO LIST

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark as Done")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(tasks):
            new_task = input("Enter new task: ")
            tasks[num-1] = new_task
            print("Task updated!")
        else:
            print("Invalid number!")

    elif choice == "4":
        show_tasks()
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted!")
        else:
            print("Invalid number!")

    elif choice == "5":
        show_tasks()
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1] = tasks[num-1] + " ✅ DONE"
            print("Marked as done!")

    elif choice == "6":
        print("Bye! Good job!")
        break

    else:
        print("Please enter 1 to 6 only!")