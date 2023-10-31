import cli
import info
from exceptions import exception
from system import core
import filesystem as fs
from filesystem import wrapper as wr
from system import downloads

def main_menu():
    loop = True
    while loop == True:
        cli.make_menu("MENU", "", style = "default", new_line = True)
        count = 0
        for i in core.LIST_MENU_ITEMS:
            count += 1
            print(f'[{count}] - {core.LIST_MENU_ITEMS[count-1]}')
        print(f'[0] - Quit {info.NAME}')
        print()
        
        try:
            opt = int(input("[?]: Type the option number: "))
            cli.separator()
            if opt > len(core.LIST_MENU_ITEMS):
                exception.Throw.invalid_option()
                return

            if opt == 0:
                cli.make_menu(info.NAME, "Application has been quit!", "long", newline = True)
                loop = False
                exit()

            if opt == 1:
                menu_new_project()
            elif opt == 2:
                core.get_project_list(core.repository_folder)
            elif opt == 3:
                print(">> NOT IMPLEMENTED <<")
            elif opt == 4:
                downloads.download_samples()
        except:
            return
        
def menu_new_project():
    cli.make_menu("NEW PROJECT", style = "default", new_line = True)
    count = 0
    for i in core.LIST_PROJECTS:
        count += 1
        print(f'[{count}] - {core.LIST_PROJECTS[count-1]}')
    print(f'[0] << Go Back')

    cli.separator()
    opt = int(input("[?]: Type the option number: "))
    cli.separator()
    if opt > len(core.LIST_PROJECTS):
        exception.Throw.invalid_option()
        return

    if opt == 0:
        pass
    if opt == 1:
        core.create(opt, "BLANK APPLICATION")
    elif opt == 2:
        core.create(opt, "MENU APPLICATION")
    elif opt == 3:
        core.create(opt, "TWITTER APPLICATION")
    elif opt == 4:
        core.create(opt, "JUPYTER NOTEBOOK")

### FUTURE VERSIONS
def menu_project_options():
    cli.make_menu("MANAGEMENT OPTION")
    count = 0
    for i in core.LIST_PROJECT_OPTIONS:
        count += 1
        print(f"[{count}]: {core.LIST_PROJECT_OPTIONS[i][0]}\n— {core.LIST_PROJECT_OPTIONS[i][1]}")
        cli.separator()
    
    opc = int(input(">>[!] Type a number: "))
    cli.separator()
    if opc == 1:
        wr.create_file("test.xml", core.repository_folder, "This is a test output")