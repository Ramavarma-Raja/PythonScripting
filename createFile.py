import os

file_path = input("Enter destination path and name : ")

if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
        pass
else:
    print("File Already exists!")