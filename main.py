def display_tasks(tasks):
    print("Tasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "✓" if task['done'] else " "
        print(f"{idx}. [{status}] {task['description']}")


def add_todo(tasks, description):
    tasks.append({'description': description, 'done': False})
    print("Task added!")


def mark_task_done(tasks, index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]['done'] = True
        print("Task marked as done!")
    else:
        print("Invalid task index!")


def main():
    tasks = []

    try:
        with open('tasks.txt', 'r') as file:
            for line in file:
                description, done = line.strip().split(',')
                tasks.append({'description': description, 'done': done == 'True'})
    except FileNotFoundError:
        print("Check your work")

    while True:
        print(" Task Menu:")
        print("Press 1 to Show Tasks")
        print("Press 2 to Add Task")
        print("Press 3 to Mark Task as Done")
        print("Press 4 to Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            description = input("Enter task description: ")
            add_todo(tasks, description)
        elif choice == '3':
           index = int(input("Enter task index to mark as done: "))
            mark_task_done(tasks, index)
        elif choice == '4':
            with open('tasks.txt', 'w') as file:
                for task in tasks:
                    file.write(f"{task['description']},{task['done']}\n")
            print("Tasks saved. Quitting...")
            break
        else:
            print("Invalid choice. Please select again.")


if __name__ == "__main__":
    main()