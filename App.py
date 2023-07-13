"""
### App.py

- This file is used to implement code used to run scripts for the bridge
"""
## App File
## This file is used to implement code used to run scripts for Mac

from system import APPINFO
from exception import Exceptions
from system import Core

def Run():
    Loop = True

    while Loop == True:
        print()
        print("="*80)
        print(">> MENU <<")
        print("="*80)
        print("[1] - New Project...")
        # print("[2] - Projects List")
        # print("[3] - Backup Projects")
        # print("[4] - Sample Projects...")
        print("[0] - Quit PyBridge")
        print()

        try:
            Opt = int(input(">>[!] Type The Item Number: "))
            print()
        except:
            Exceptions.Throw.InputFormat()

        if Opt == 0:
            Loop = False
            print("=" * 80)
            # print("[PyBridge for Mac] - Quit")
            print(f'[{APPINFO.NAME}] - Quit')
            print("=" * 80)
            try:
                quit()
            except:
                return

        elif Opt == 1:
            NewProjectMenu()

        elif Opt == 2:
            Core.ProjectList()
            
        elif Opt == 3:
            Core.Backup()

        elif Opt == 4:
            print(">> Module not installed")
        else:
            Exceptions.Throw.InvalidOption()

def NewProjectMenu():
    print("="*80)
    print(">> NEW PROJECT <<")
    print("="*80)
    print("[1] - Create Blank Project")
    print("[2] - Create a Menu Application Loop Project")
    print("[3] - Create Twitter Application Project")
    print("[4] - Create a Jupyter Notebook")
    print("[0] - << Go Back")
    print()

    try:
        Opt = int(input(">>[!] Type The Item Number: "))
        print()
    except:
        Exceptions.Throw.InputFormat()

    if Opt == 0:
        return

    elif Opt == 1:
        Core.ProjectOption = 1
        Core.ProjectType = "PyBridge Blank Project"
        Core.CreateBridge()

    elif Opt == 2:
        Core.ProjectOption = 2
        Core.ProjectType = "Menu Application Loop Project"
        Core.CreateBridge()

    elif Opt == 3:
        Core.ProjectOption = 3
        Core.ProjectType = "Twitter Application Project"
        Core.CreateBridge()

    elif Opt == 4:
        Core.ProjectOption = 4
        Core.ProjectType = "Jupyter Notebook Project"
        Core.CreateBridge()

    else:
        Exceptions.Throw.InvalidOption()
    # except:
    #     Exceptions.Throw.InputFormat()