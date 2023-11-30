import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir ="C:\Users\Dell\Downloads\New folder"
to_dir="C:/Users/Dell/Downloads/test"
class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"hey,{event.src_path} has been created!")

    def on_modified(self,event):
        print(f"your file has modified{event.src_path}!")    

    def on_moved(self,event):
        print(f"your file has moved or renamed{event.src_path}!")

    def on_deleted(self,event):
        print(f"oops! Someone deleted{event.src_path}!")

# Initialize Event Handler Class
event_handler = FileEventHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
 while True:
    time.sleep(2)
    print("running...")

except KeyboardInterrupt:
    print("stopped!")
    observer.stop()