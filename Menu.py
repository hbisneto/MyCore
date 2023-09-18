import APPINFO
import CLI
import App
from exception import Exceptions

itemslist = [
    "New Project",
    "Project List",
    "Backup Projects",
    "Sample Projects"
]

def menu():
    count = 0
    for i in itemslist:
        count += 1
        print(f'[{count}] - {itemslist[count-1]}')
    print(f'[0] - Quit {APPINFO.NAME}')
    print()

def userInput():
    try:
        opt = int(input("[?]: Type the option number: "))
        CLI.separator()
        if opt > len(itemslist):
            Exceptions.Throw.InvalidOption()
            return

        if opt == 0:
            CLI.showMenu(APPINFO.NAME, "Application has been quit!", "long", newline = True)
            App.loop = False
            exit()

        if opt == 1:
            print(">> Option 1")
        elif opt == 2:
            print(">> Option 2")
        elif opt == 3:
            print(">> Option 3")
        elif opt == 4:
            print(">> Option 4")
    except:
        return