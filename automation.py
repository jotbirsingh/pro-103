import os 
import shutil
from_dir = "C:\Users\Dell\Downloads\New folder"
to_dir="C:/Users/Dell/Downloads/test"
list_of_files=os.listdir(from_dir)
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    if(extension==""):
        continue
    if(extension in [".gif",".png",".jpg",".jpeg"]):
        pathone=from_dir+"/"+file_name
        pathtwo=to_dir+"/"+"doc_file"
        paththree=to_dir+"/"+"doc_file"+"/"+file_name
        if(os.path.exists(pathtwo)):
            print("moving")
            shutil.move(pathone,paththree)
        else:
            os.makedirs(pathtwo)
            print("moving")
            shutil.move(pathone,paththree)