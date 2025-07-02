
#helpmodules
#get_next_id
#slow_print
import time
import os
import json
import python_keys as pk

#to ensure the files exist in a new setup 
def ensure_setup():
    #data setup
    required_dirs = ["diary_entries"]#files=directories
    required_files = ["notes.txt", "id_counter.txt", "taskpending.json","python_keys.json"]#txt or json files

    for directory in required_dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)

    if not os.path.exists("taskpending.json"):
        with open("taskpending.json", "w") as f:
            f.write("[]")
    
    if not os.path.exists("python_keys.json"):
        with open("python_keys.json", "w") as f:
            f.write("[]")

    if not os.path.exists("emotion_log.json"):
        with open("emotion_log.json", "w") as f:
            f.write("[]")

    if not os.path.exists("expenditure.json"):
        with open("expenditure.json", "w") as f:
            f.write("{}")

    

    if not os.path.exists("id_counter.txt"):
        with open("id_counter.txt", "w") as f:
            f.write("0")
    
    if not os.path.exists("id_counter_python.txt"):
        with open("id_counter_python.txt", "w") as f:
            f.write("0")


def write_json(filename,data):
    with open(filename,"w") as f:
        json.dump(data,f,indent=2)


def write_txt(filename,data):
    with open(filename, "w") as f:
        f.write(data)
        
#adds a new thing to dictionary
def append_json(filename,new_entry):
    data=pk.load_json(filename)
    data.update(new_entry)
    write_json(filename,data)
    slow_print("Data Stored")



# ID generator
def get_next_id():
    with open("id_counter.txt", "r") as f:
        last_id = int(f.read().strip())
    new_id = last_id + 1
    with open("id_counter.txt", "w") as f:
        f.write(str(new_id))
    return f"[{new_id}]"

def get_next_id_python():
    with open("id_counter_python.txt","r") as f:
        last_id = int(f.read().strip())
    new_id = last_id + 1
    with open("id_counter_python.txt", "w") as f:
        f.write(str(new_id))
    return f"[{new_id}]"
        

# Human interface: prints text slowly like a curtain revealing info
def slow_print(text, delay=0.05):  # delay per character
    for char in str(text):  # Make sure even non-string data prints correctly
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # newline at end
