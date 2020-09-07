# Easy Backup program 
# Author: Pratyaksha Beri
# v0.5
import os
items = os.listdir()
items.remove('easy-backup.py')
print(f"backing up {items}")
os.system("mkdir backup")
os.chdir("backup")
for item in items:
	command = "mkdir "+ item
	os.system(command)
	command2 = "cp "+ item +" backup/"+item
os.system("zip -r backup.zip backup/")
os.system("rm -r backup")
