import APPINFO
import App
import CLI
import FileSystem
from exception import Exceptions
from system import Core
from system import Services

menuList = [
    "New Project",
    "Project List",
    "Backup Projects",
    "Sample Projects"
]

newProjectList = [
    "Create Blank Project",
    "Create a Menu Application",
    "Create a Twitter Application",
    "Create a Jupyter Notebook"
]

def menu():
    CLI.showMenu("MENU", "", style = "default", newline = True)
    count = 0
    for i in menuList:
        count += 1
        print(f'[{count}] - {menuList[count-1]}')
    print(f'[0] - Quit {APPINFO.NAME}')
    print()
    
    try:
        opt = int(input("[?]: Type the option number: "))
        CLI.separator()
        if opt > len(menuList):
            Exceptions.Throw.InvalidOption()
            return

        if opt == 0:
            CLI.showMenu(APPINFO.NAME, "Application has been quit!", "long", newline = True)
            App.loop = False
            exit()

        if opt == 1:
            print(">> Option 1")
            newProjectMenu()
        elif opt == 2:
            print(">> Option 2")
            FileSystem.getProjectList()
        elif opt == 3:
            print(">> Option 3")
        elif opt == 4:
            # print(">> Option 4")
            Services.DownloadSamplesMenu()
    except:
        return
    
def newProjectMenu():
    CLI.showMenu("NEW PROJECT", style = "default", newline = True)
    count = 0
    for i in newProjectList:
        count += 1
        print(f'[{count}] - {newProjectList[count-1]}')
    print(f'[0] << Go Back')
    print()

    try:
        opt = int(input("[?]: Type the option number: "))
        CLI.separator()
        if opt > len(newProjectList):
            Exceptions.Throw.InvalidOption()
            return

        if opt == 0:
            pass
            # CLI.showMenu(APPINFO.NAME, "Application has been quit!", "long", newline = True)
            # App.loop = False
            # exit()
        if opt == 1:
            print(">> Option 1")
            Core.CreateBridge(opt, "BLANK APPLICATION")
        elif opt == 2:
            print(">> Option 2")
        elif opt == 3:
            print(">> Option 3")
        elif opt == 4:
            print(">> Option 4")
            Core.CreateBridge(opt, "JUPYTER NOTEBOOK")
    except:
        return