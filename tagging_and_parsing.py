import json
import datetime
import re
import helpmodules as hp
import emotional_filing_for_introspection as ei

today = datetime.date.today()
task_file = "taskpending.json"

def load_tasks():
    with open(task_file, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(task_file, "w") as f:
        json.dump(tasks, f, indent=2)

def tag_parser(entry):
    if not entry:
        hp.slow_print("No tags found.")
        return

    filename = f"notes_{today.strftime('%Y-%m-%d')}.txt"
    tags = re.findall(r"@(\w+)\((.*?)\)", entry)

    for tag, content in tags:
        content = content.strip()
        if tag == "tasks":
            task_id = hp.get_next_id()
            task = {"id": task_id, "task": content, "tag": "UN", "due": None}
            tasks = load_tasks()
            tasks.append(task)
            save_tasks(tasks)
            hp.slow_print(f"[Task] {task_id}: {content}")
        elif tag == "emotions":
            hp.slow_print(f"[Emotion Logged]: {content}")
            emotions=ei.parse_emotion_tag(content)
            primary_emo=emotions[0]
            secondary_emo=emotions[1]
            ei.log_new_entry(primary_emo,secondary_emo)
        else:
            hp.slow_print(f"[{tag.capitalize()}] {content}")

def add_task():
    content = input("Enter task: ").strip().split(",")
    for t in content:
        if content:
            task_id= hp.get_next_id()
            tasks = load_tasks()
            tasks.append({"id": task_id, "task": content, "tag": "UN", "due": None})
            save_tasks(tasks)
            hp.slow_print(f"Task added with ID {task_id}")
        else:
            hp.slow_print("Empty task not added.")

    

def remove_task(task_id_to_remove):
    tasks = load_tasks()
    updated_tasks = [t for t in tasks if t["id"] != task_id_to_remove]
    if len(tasks) == len(updated_tasks):
        hp.slow_print("No task was removed.")
    else:
        save_tasks(updated_tasks)
        hp.slow_print(f"Task {task_id_to_remove} removed.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        hp.slow_print("No tasks pending.")
    else:
        for task in tasks:
            line = f"{task['id']} - {task['task']} [{task['tag']}]"
            if task["due"]:
                line += f" (Due: {task['due']})"
            hp.slow_print(line)

def tag_all_pending_tasks():
    tasks = load_tasks()
    for task in tasks:
        hp.slow_print(f"Task: {task['task']}")
        imp = input("Is it important? (i/n): ").strip().lower()
        urg = input("Is it urgent? (u/n): ").strip().lower()

        if imp == "i" and urg == "u":
            task["tag"] = "UI"
            task["due"] = input("Due date (YYYY-MM-DD): ").strip()
        elif imp == "i" and urg == "n":
            task["tag"] = "NI"
        elif imp == "n" and urg == "u":
            task["tag"] = "UN"
            task["due"] = input("Due date (YYYY-MM-DD): ").strip()
        elif imp == "n" and urg == "n":
            task["tag"] = "NN"
        else:
            task["tag"] = "Uncategorized"
    save_tasks(tasks)
    hp.slow_print("All tasks have been tagged.")

def task_list():
    desired_tag = input("Retrieve tasks with tag (UI/NI/UN/NN): ").strip().upper()
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["tag"] == desired_tag:
            hp.slow_print(f"{task['id']} - {task['task']} (Due: {task.get('due', 'None')})")
            found = True
    if not found:
        hp.slow_print("No tasks found with that tag.")
