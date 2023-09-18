import CLI
import Menu

loop = True
def start():
    while loop == True:
        CLI.showMenu("Menu", "", style = "default", newline = True)
        Menu.menu()
        Menu.userInput()