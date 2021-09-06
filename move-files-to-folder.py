from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# pip install watchdog

import os
import json
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            split_tup = os.path.splitext(filename)
            src = folder_to_track + "/" + filename
            folder_name = split_tup[1].replace(".", "")
            if not os.path.exists(folder_destination + "/" + folder_name):
                os.makedirs(folder_destination + "/" + folder_name)
            if split_tup != "":
                new_destination = (
                    folder_destination + "/" + folder_name + "/" + filename
                )
            else:
                new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)


folder_to_track = "/home/ogeshwary/Downloads"
folder_destination = "/home/ogeshwary/Downloads"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
