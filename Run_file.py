import tagging_and_parsing_new as tp
import helpmodules as hp
hp.ensure_setup()
hp.slow_print("What would you like to do")

command=input(" (view/add/remove/tag): ").strip().lower()
if command == "view":
    tp.view_tasks()
elif command == "add":
    tp.add_task()
elif command == "remove":
    task_id_to_remove = input("Enter the task ID to remove: ").strip()
    tp.remove_task(task_id_to_remove)
elif command == "tag":
    tp.tag_all_pending_tasks()
else:
    hp.slow_print("Invalid command. Please enter 'view', 'remove', or 'tag'.")
