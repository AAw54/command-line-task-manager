import json

# Global variables
exit_program = False
tasks = []
file_name = "tasks.json"

# Task manager functions

def add_task():
    task_name = input("Enter new task name: ")
    tasks.append({"name": task_name, "done": False})
    print("**Task added successfully")
    input("Press Enter to continue...")
    
def view_tasks():
    if len(tasks) == 0:
        print("**No tasks available.")
    else:
        print("\n==== Task List ====")
        for x in range(len(tasks)):
            if tasks[x]["done"]:
                done = "[✓]"
            else:
                done = "[ ]"
            print(f"{x+1}. {done} {tasks[x]['name']}")
        print()
    input("Press Enter to continue...")

def mark_done():
    if len(tasks) == 0:
        print("**No tasks available")
    else:
        task_number = input("Enter task number: ")
        if task_number.isdigit():
            task_number = int(task_number)
            if task_number > len(tasks) or task_number < 1:
                print("**Invalid input")
            else:
                tasks[task_number - 1]["done"] = True
                print("**Task marked successfully")
        else:
            print("**Invalid input")
    input("Press Enter to continue...")

def remove_task():
    if len(tasks) == 0:
        print("**No tasks available")
    else:
        task_number = input("Enter task number to delete: ")
        if task_number.isdigit():
            task_number = int(task_number)
            if task_number >= 1 and task_number <= len(tasks):
                tasks.pop(task_number - 1)
                print("**Successfully removed task:", task_number)
            else:
                print("**Invalid input")
        else:
            print("**Invalid input")
    input("Press Enter to continue...")

def save_tasks():
    # Save current tasks to the JSON file
    with open(file_name, "w") as file:
        json.dump(tasks, file)

# Load tasks if the file already exists
try:
    with open(file_name) as file:
        tasks = json.load(file)

except FileNotFoundError:
    print("**No saved tasks found.")
except json.JSONDecodeError:
    print("**Task file is empty or corrupted.")

print("\nWelcome to Task Manager!")

# Main program loop
try:

    while not exit_program:
        
        print("\n==== Task Manager ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Done")
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Choose: ")

        # Check if menu input is a number
        if choice.isdigit():
            num = int(choice)

            if num > 5 or num < 1:
                print("**Invalid number")
                continue

            # Valid choice
            if num == 1:
                add_task()
                
            elif num == 2:
                view_tasks()

            elif num == 3:
                mark_done()

            elif num == 4:
                remove_task()
                
            elif num == 5:
                exit_program = True

        # Invalid non-numeric input
        else:
            print("**Input should be a number")
finally:
    save_tasks()
    print("**Tasks saved!")

print("Thank you for using Task Manager.")


