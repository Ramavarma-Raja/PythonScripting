import os

disk = input("Enter Drive to have its Space Monitored : ")

if os.name == "linux" or os.name == "posix":
    os.system(f"df -h {disk}")
elif os.name == "nt":
    try:
        if disk != "":
            os.system(f"wmic logicaldisk where deviceid='{disk}:' get name, size, freespace")
        else:
            os.system(f"wmic logicaldisk get name, size, freespace")
    except OSError as error:
        print(error)
        print("OS Error")