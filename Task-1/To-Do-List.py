import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename='todo.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, title, description='', due_date=None):
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'due_date': due_date,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.tasks.append(task)
        self.save_tasks()
        return task

    def list_tasks(self, show_completed=False):
        return [task for task in self.tasks if show_completed or not task['completed']]

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                task['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_tasks()
                return task
        return None

    def update_task(self, task_id, title=None, description=None, due_date=None):
        for task in self.tasks:
            if task['id'] == task_id:
                if title:
                    task['title'] = title
                if description:
                    task['description'] = description
                if due_date:
                    task['due_date'] = due_date
                task['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_tasks()
                return task
        return None

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()
        return True

def display_menu():
    print("\nTodo List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        status = "✓" if task['completed'] else " "
        due_date = f" (Due: {task['due_date']})" if task['due_date'] else ""
        print(f"{task['id']}. [{status}] {task['title']}{due_date}")
        if task['description']:
            print(f"   {task['description']}")
        print(f"   Created: {task['created_at']} | Updated: {task['updated_at']}")

def main():
    todo = TodoList()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter description (optional): ")
            due_date = input("Enter due date (YYYY-MM-DD, optional): ")
            todo.add_task(title, description, due_date if due_date else None)
            print("Task added successfully!")
        
        elif choice == '2':
            show_completed = input("Show completed tasks? (y/n): ").lower() == 'y'
            tasks = todo.list_tasks(show_completed)
            display_tasks(tasks)
        
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as complete: "))
            if todo.complete_task(task_id):
                print("Task marked as complete!")
            else:
                print("Task not found.")
        
        elif choice == '4':
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new title (leave empty to keep current): ")
            description = input("Enter new description (leave empty to keep current): ")
            due_date = input("Enter new due date (YYYY-MM-DD, leave empty to keep current): ")
            
            result = todo.update_task(
                task_id,
                title if title else None,
                description if description else None,
                due_date if due_date else None
            )
            
            if result:
                print("Task updated successfully!")
            else:
                print("Task not found.")
        
        elif choice == '5':
            task_id = int(input("Enter task ID to delete: "))
            if todo.delete_task(task_id):
                print("Task deleted successfully!")
            else:
                print("Task not found.")
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
