from get_params import (DATA_DIR)
import os
import time

log_filename = "log.csv"

def init_log_file ():
    if os.path.exists(os.path.join(DATA_DIR, log_filename)):
        os.remove(os.path.join(DATA_DIR, log_filename))
    with open(os.path.join(DATA_DIR, log_filename), "a+") as fp:
        fp.write("message_type;time;message" + "\n")

def write_log (message_type: str, message: str):
    string = message_type + ";" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + ";" + message
    with open(os.path.join(DATA_DIR, log_filename), "a+") as fp:
        fp.write(string + "\n")
    print(string)