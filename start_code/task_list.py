
# As a user, to manage my task list I would like a program that allows me to:

# 1. Print a list of uncompleted tasks

# 2. Print a list of completed tasks

# 3. Print a list of all task descriptions

# 4. Print a list of tasks where time_taken is at least a given time

# 5. Print any task with a given description

### Extension

# 6. Given a description update that task to mark it as complete.

# 7. Add a task to the list
tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


def print_uncompleted_tasks():
    incomplete = []
    for task in tasks: 
        if task["completed"] == False:
          incomplete.append(task)
    print(incomplete)

print_uncompleted_tasks()  

def print_completed_tasks():
    complete = []
    for task in tasks: 
        if task["completed"] == True:
          complete.append(task)
    print(complete)

print_completed_tasks()

def print_task_descriptions():
    descriptions = []
    for task in tasks: 
        descriptions.append(task["description"])
    print(descriptions)

print_task_descriptions()

def print_minimum_time_tasks(time):
    longer_tasks = []
    for task in tasks:
        if task["time_taken"] > time:
            longer_tasks.append(task)
    print(longer_tasks)

print_minimum_time_tasks(30)

def print_described_task(description):
    described_task = []
    for task in tasks:
        if task["description"] == description:
            described_task.append(task)
    print(described_task)

print_described_task("Walk Dog")    


def Mark_complete(description):
    for task in tasks:
        if task["description"] == description:
            task["completed"] = True

Mark_complete("Feed Cat")
print(tasks)

def add_task(description, completed, time):
    tasks.append({"description": description, "completed": completed, "time_taken": time})

add_task("Shower", True, 10)
print(tasks)