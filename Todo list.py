class TodoList:
    def __init__(self):

        self.tasks = []

    def add_task(self, task):
       
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def remove_task(self, task):
        found = False
        for item in self.tasks:
            if item["task"] == task:
                self.tasks.remove(item)
                print(f"Task '{task}' removed.")
                found = True
                break
        if not found:
            print("Task not found.")

    def mark_completed(self, task):
        found = False
        for item in self.tasks:
            if item["task"] == task:
                item["completed"] = True
                print(f"Task '{task}' marked as completed.")
                found = True
                break
        if not found:
            print("Task not found.")

    def update_task(self, old_task, new_task):
        found = False
        for item in self.tasks:
            if item["task"] == old_task:
                item["task"] = new_task
                print(f"Task '{old_task}' updated to '{new_task}'.")
                found = True
                break
        if not found:
            print("Task not found.")

    def clear_tasks(self):
        self.tasks = []
        print("All tasks cleared.")

    def show_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\n--- Your To-Do List ---")
            for i, item in enumerate(self.tasks, 1):
                if item["completed"]:
                    print(f"{i}. [COMPLETED] {item['task']}")
                else:
                    print(f"{i}. {item['task']}")
            print("-----------------------\n")

# Main Program
todo = TodoList()

while True:
    print("\n ========= TO-DO LIST MENU ==========")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Clear All Tasks")
    print("6. Show Tasks")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        task = input("Enter the task to add: ")
        todo.add_task(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        todo.remove_task(task)
    elif choice == "3":
        task = input("Enter the task to mark as completed: ")
        todo.mark_completed(task)
    elif choice == "4":
        old_task = input("Enter the task to update: ")
        new_task = input("Enter the new task description: ")
        todo.update_task(old_task, new_task)
    elif choice == "5":
        todo.clear_tasks()
    elif choice == "6":
        todo.show_tasks()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-7.")