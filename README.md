# Command-Line Task Manager

A command-line task manager built in Python that enables users to create, view, update, and delete tasks. The application uses a JSON file for persistent data storage and includes input validation to ensure reliable user interaction.


## Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Data stored in `tasks.json`
* Input validation for user commands

## Demo

```bash
Welcome to Task Manager!

==== Task Manager ====
1. Add Task
2. View Tasks
3. Mark Done
4. Remove Task
5. Exit
Choose: 2

==== Task List ====
1. [ ] Study Python loops
2. [ ] Read about data structures
3. [ ] Review lecture notes
4. [ ] Plan next study session

Press Enter to continue...

==== Task Manager ====
1. Add Task
2. View Tasks
3. Mark Done
4. Remove Task
5. Exit
Choose: 1
Enter new task name: Revise algorithms concepts
Task added successfully
Press Enter to continue...

==== Task Manager ====
1. Add Task
2. View Tasks
3. Mark Done
4. Remove Task
5. Exit
Choose: 2

==== Task List ====
1. [ ] Study Python loops
2. [ ] Read about data structures
3. [ ] Review lecture notes
4. [ ] Plan next study session
5. [ ] Revise algorithms concepts

Press Enter to continue...

==== Task Manager ====
1. Add Task
2. View Tasks
3. Mark Done
4. Remove Task
5. Exit
Choose: 3
Enter task number: 4
Task marked successfully
Press Enter to continue...

==== Task Manager ====
1. Add Task
2. View Tasks
3. Mark Done
4. Remove Task
5. Exit
Choose: 2

==== Task List ====
1. [ ] Study Python loops
2. [ ] Read about data structures
3. [ ] Review lecture notes
4. [✓] Plan next study session
5. [ ] Revise algorithms concepts

Press Enter to continue...

==== Task Manager ====
1. Add Task
2. View Tasks
3. Mark Done
4. Remove Task
5. Exit
Choose: 5
Tasks saved!
Thank you for using Task Manager.
```

## Technologies Used

* Python
* JSON

## How to Run

```bash
git clone https://github.com/Aaw54/command-line-task-manager.git
cd command-line-task-manager
python task_manager.py
```

## Project Structure

* `task_manager.py` → main application
* `tasks.json` → stores task data

## Author

Aaesha Aldahmani
