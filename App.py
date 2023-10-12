# import Menu
import Cli
import Info
from exception import Exceptions
from system import Core as core
from system import FileSystem as fs
from system import Downloads

def menu():
    loop = True
    while loop == True:
        Cli.make_menu("MENU", "", style = "default", newline = True)
        count = 0
        for i in core.LIST_MENU_ITEMS:
            count += 1
            print(f'[{count}] - {core.LIST_MENU_ITEMS[count-1]}')
        print(f'[0] - Quit {Info.NAME}')
        print()
        
        try:
            opt = int(input("[?]: Type the option number: "))
            Cli.separator()
            if opt > len(core.LIST_MENU_ITEMS):
                Exceptions.Throw.invalid_option()
                return

            if opt == 0:
                Cli.make_menu(Info.NAME, "Application has been quit!", "long", newline = True)
                loop = False
                exit()

            if opt == 1:
                print(">> Option 1")
                menu_new_project()
            elif opt == 2:
                print(">> Option 2")
                fs.get_project_list(fs.repository)
            elif opt == 3:
                print(">> Option 3")
            elif opt == 4:
                Downloads.download_samples()
        except:
            return

def menu_new_project():
    Cli.make_menu("NEW PROJECT", style = "default", newline = True)
    count = 0
    for i in core.LIST_PROJECTS:
        count += 1
        print(f'[{count}] - {core.LIST_PROJECTS[count-1]}')
    print(f'[0] << Go Back')

    Cli.separator()
    opt = int(input("[?]: Type the option number: "))
    Cli.separator()
    if opt > len(core.LIST_PROJECTS):
        Exceptions.Throw.invalid_option()
        return

    if opt == 0:
        pass
    if opt == 1:
        print(">> Option 1")
        core.create(opt, "BLANK APPLICATION")
    elif opt == 2:
        print(">> Option 2")
    elif opt == 3:
        print(">> Option 3")
    elif opt == 4:
        print(">> Option 4")
        core.create(opt, "JUPYTER NOTEBOOK")

def start():
    menu()