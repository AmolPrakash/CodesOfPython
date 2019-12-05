import os, os.path  
QUIT = '7'
COMMANDS = ('1', '2', '3', '4', '5', '6', '7')

MENU = """1 List the current directory
    2 Move up
    3 Move down
    4 Number of files in the directory
    5 Size of the directory in bytes
    6 Search for a filename
    7 Quit the program"""

def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print ("have a nice day")
            break
def acceptCommand():
    command = input("enter a number : ")
    if command in COMMANDS:
        return command
    else:
        print("error not recognised")
        return acceptcommand()
    
def runCommand():
    if command == "1":
        listCurrentDir(os.getced())
        
def listCurrentDir(dirName):
    lyst = os.listdir(dirName)
    for element in lyst:
        print (element)

if __name__ == "__main__":
    main()
    
