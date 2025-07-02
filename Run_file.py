import tagging_and_parsing_new as tp
import helpmodules as hp

hp.slow_print("What would you like to do")

command=input(" (view/add/remove/tag): ").strip().lower()
if command == "view":
    tp.view_tasks()
elif command == "add":
    enter_tasks=input("Enter your tasks:")#use a comma to split the tasks
    task=enter_tasks.split(",")
    for t in task:
        t=t.strip()
        if t:
            tp.add_task(t)
            print("Task added successfully.")
        else:
            hp.slow_print("Empty task not added.")
    
elif command == "remove":
    task_id_to_remove = input("Enter the task ID to remove: ").strip()
    tp.remove_task(task_id_to_remove)
elif command == "tag":
    tp.tag_all_pending_tasks()
else:
    hp.slow_print("Invalid command. Please enter 'view', 'remove', or 'tag'.")

