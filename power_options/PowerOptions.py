#Importing os for commands and platform for defining pc os
import os 
import platform

#shutdown function where we filtering users os and giving command
def shutdown():
    if platform.system() == "Windows":
        os.system("shutdown -s")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("shutdown -h now")
    else:
        print("Os not supported")


#restart function where we filtering users os and giving command
def restart():
    if platform.system() == "Windows":
        os.system("shutdown /r")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("reebot now")
    else:
        print("Os not supported")
    
#taking input from user and taking it on lowercase
command = input("Use \'r\' for restart and \'s\' for shutdown: ").lower()

if command == "r":
    restart()
elif command == "s":
    shutdown()
else:
    print("Wrong letter")
