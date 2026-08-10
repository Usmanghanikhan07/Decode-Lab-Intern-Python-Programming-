
// ========TO DO LIST PROJECT========

def display_menu():
    print("\n" + "=" * 40)
    print("         TO-DO LIST APPLICATION")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("=" * 40)


def add_task(tasks):
    task = input("Enter a task: ").strip()
    if task:
        tasks.append(task)
        print(f" Task '{task}' added successfully.")
    else:
        print("❌ Task cannot be empty.")


def view_tasks(tasks):
    print("\n------ YOUR TASKS ------")
    if not tasks:
        print("No tasks available.")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("\nEnter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f" Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("\nThank you for using the To-Do List App.")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
