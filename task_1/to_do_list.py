def show_menu():
    print("***** TO DO LIST *****")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task Status (Mark Completed)")
    print("4. Delete Task")
    print("5. Exit")

def task_app():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            if not tasks:
                print("Your to-do list is empty,Add tasks")
            else:
                print("----- YOUR TASKS -----")
                for idx, task in enumerate(tasks, 1):
                    status = "Done" if task['completed'] else " Pending"
                    print(f"{idx}. {task['title']} [{status}]")
        
        elif choice == '2':
            title = input("Enter the task title: ").strip()
            if title:
                tasks.append({'title': title, 'completed': False})
                print(f"Task '{title}' added successfully!")
            else:
                print("Task title cannot be empty.")
        elif choice == '3':  
                 
            if not tasks:
                print("No tasks to update.")
                continue
            try:
                task_num = int(input("Enter task number to mark completed: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]['completed'] = True
                    print(f"Task {task_num} marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '4':
            if not tasks:
                print("No tasks to delete.")
                continue
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Removed task: '{removed['title']}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '5':
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice! Please select between 1 and 5.")

if __name__ == "__main__":
    task_app()