from get_params import (IS_EXPORT)
from export import export
from logs import init_log_file, write_log

init_log_file()
write_log("[START]","Start main.py")
if IS_EXPORT:
    export()
write_log("[FINISH]","Finish main.py")