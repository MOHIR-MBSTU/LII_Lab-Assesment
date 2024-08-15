import sys

# To-Do List Application
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
            print("")

    def show_menu(self):
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

def main():
    todo_list = ToDoList()

    while True:
        todo_list.show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            task = input("Enter the task: ").strip()
            if task:
                todo_list.add_task(task)
            else:
                print("Task cannot be empty.")
        elif choice == '2':
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to remove: ")) - 1
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Exiting the To-Do List application.")
            sys.exit()
        else:
            print("Invalid option. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
