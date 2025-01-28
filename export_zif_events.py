from logs import write_log
from https_headers import get_headers
from get_params import (CLIENT_ID, CLIENT_SECRET, ZIF_EVENTS_API, EVENTS_DIR, EVENTS_TYPES_DIR, EVENTS_STATUSES_DIR)
import os
import shutil
from export_array_from_endpoint import export_array_from_endpoint

if os.path.exists(EVENTS_DIR):
    shutil.rmtree(EVENTS_DIR)
else:
    os.makedirs(EVENTS_DIR, exist_ok=True)

def export_zif_events():
    write_log("[START]","Start export_zif_events.py")
    header = get_headers(CLIENT_ID, CLIENT_SECRET)
    export_array_from_endpoint(ZIF_EVENTS_API, "/eventstatuses", header, EVENTS_STATUSES_DIR, "content")
    export_array_from_endpoint(ZIF_EVENTS_API, "/eventtypes", header, EVENTS_TYPES_DIR, "content")
    write_log("[FINISH]","Finish export_zif_events.py")