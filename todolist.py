class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added to the to-do list.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{index}. {task['task']} - {status}")

    def mark_as_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print(f"Task '{self.tasks[task_index - 1]['task']}' marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task['task']}' deleted from the to-do list.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            task_index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_as_completed(task_index)

        elif choice == '4':
            task_index = int(input("Enter the task index to delete: "))
            todo_list.delete_task(task_index)

        elif choice == '5':
            print("Exiting the To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
