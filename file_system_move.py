import os

file_path = "main.txt"
dest = "newfile.txt"


os.rename(file_path,dest)

print("main.txt has been renamed")
