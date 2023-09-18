"""
FileSystem.py

- This file contains some default directories of your system
- You can use this file to implement custom directories used by your application
"""
## FileSystem
## This file contains some default directories of your system
## You can use this file to implement custom directories used by your application

### NATIVE LIBRARIES ###
import os
from sys import platform
import APPINFO
### NATIVE LIBRARIES ###

### GLOBAL VARIABLES ###
CurrentPath = os.getcwd()
### GLOBAL VARIABLES ###

## LINUX
if platform == "linux" or platform == "linux2":
    User = f'/home/{os.environ["USER"]}'
    Desktop = f'{User}/Desktop'
    Documents = f'{User}/Documents'
    Downloads = f'{User}/Downloads'
    Music = f'{User}/Music'
    Pictures = f'{User}/Pictures'
    Public = f'{User}/Public'
    Videos = f'{User}/Videos'
## MAC
elif platform == "darwin":
    User = f'/Users/{os.environ["USER"]}'
    Desktop = f'{User}/Desktop'
    Documents = f'{User}/Documents'
    Downloads = f'{User}/Downloads'
    Music = f'{User}/Music'
    Pictures = f'{User}/Pictures'
    Public = f'{User}/Public'
    Videos = f'{User}/Movies' ## POINT TO MOVIES FOLDER ON macOS
## WINDOWS
elif platform == "win32" or platform == "win64":
    User = os.environ['USERPROFILE']
    Desktop = f'{User}/Desktop'
    Documents = f'{User}/Documents'
    Downloads = f'{User}/Downloads'
    Music = f'{User}/Music'
    Pictures = f'{User}/Pictures'
    Public = os.environ['PUBLIC']
    Videos = f'{User}/Videos'

### CUSTOM VARIABLES ###
## LINUX
linux_Templates = f'{User}/Templates'

## MAC
mac_Applications = f'{User}/Applications'
mac_Movies = f'{User}/Movies' # JUST IN CASE...

## WINDOWS
windows_ApplicationData = f'{User}/AppData/Roaming'
windows_LocalAppData = f'{User}/AppData/Local'
windows_Temp = f'{windows_LocalAppData}/Temp'
windows_Favorites = f'{User}/Favorites'

## MY VARIABLES
AppFolder = f'{Documents}/{APPINFO.NAME}'
Repository = f'{AppFolder}/Repository'
## MY VARIABLES
### CUSTOM VARIABLES ###

### FUNCTIONS ###
def CreateEnvironmentFolders():
    try:
        os.mkdir(AppFolder)
        print(f'>> {APPINFO.NAME}: "{AppFolder}" created')
    except:
        pass

    try:
        os.mkdir(Repository)
        print(f'>> {APPINFO.NAME}: "{Repository}" created')
    except:
        pass

def ProjectList():
    print("Hellow orld")
### FUNCTIONS ###