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
import codecs
from sys import platform
### NATIVE LIBRARIES ###

### PYBRIDGE LIBRARIES
import Cli
from exception import Exceptions
### PYBRIDGE LIBRARIES

### GLOBAL VARIABLES ###
CURRENT_LOCATION = os.getcwd()
### GLOBAL VARIABLES ###

## LINUX
if platform == "linux" or platform == "linux2":
    PLATFORM_NAME = "Linux"
    user = f'/home/{os.environ["USER"]}'
    desktop = f'{user}/Desktop'
    documents = f'{user}/Documents'
    downloads = f'{user}/Downloads'
    music = f'{user}/Music'
    pictures = f'{user}/Pictures'
    public = f'{user}/Public'
    videos = f'{user}/Videos'
## MAC
elif platform == "darwin":
    PLATFORM_NAME = "Mac"
    user = f'/Users/{os.environ["USER"]}'
    desktop = f'{user}/Desktop'
    documents = f'{user}/Documents'
    downloads = f'{user}/Downloads'
    music = f'{user}/Music'
    pictures = f'{user}/Pictures'
    public = f'{user}/Public'
    videos = f'{user}/Movies' ## POINT TO MOVIES FOLDER ON macOS
## WINDOWS
elif platform == "win32" or platform == "win64":
    PLATFORM_NAME = "Windows"
    user = os.environ['USERPROFILE']
    desktop = f'{user}/Desktop'
    documents = f'{user}/Documents'
    downloads = f'{user}/Downloads'
    music = f'{user}/Music'
    pictures = f'{user}/Pictures'
    public = os.environ['PUBLIC']
    videos = f'{user}/Videos'

### CUSTOM VARIABLES ###
## LINUX
linux_templates = f'{user}/Templates'

## MAC
mac_applications = f'{user}/Applications'
mac_movies = f'{user}/Movies' # JUST IN CASE...

## WINDOWS
windows_applicationData = f'{user}/AppData/Roaming'
windows_localappdata = f'{user}/AppData/Local'
windows_temp = f'{windows_localappdata}/Temp'
windows_favorites = f'{user}/Favorites'





## MY VARIABLES
backup_folder = f'{CURRENT_LOCATION}/Backup'
samples_folder = f'{CURRENT_LOCATION}/Samples'
# list_projects = []
repository = f'{documents}/MyCore/Repository'
## MY VARIABLES
### CUSTOM VARIABLES ###

### FUNCTIONS ###
def create_required_folder(folder_location, folder_name=""):
    try:
        os.mkdir(f'{folder_location}')
        if len(folder_name) != 0:
            print(f'>> {folder_name}: "{folder_location}" created')
    except:
        pass

def create_backup_folder():
    """Creates the 'Backup' folder in the root of the project
    """
    try:
        os.mkdir(backup_folder)
    except:
        pass

def create_samples_folder():
    try:
        os.mkdir(samples_folder)
    except:
        pass

def create_custom_file(file_name, url, text):
    """
        filename: The name of the file you want to create, including its extension.
        url: The directory where the file will be created.
        text: The content that will be written into the file.
    """

    try:
        with codecs.open(f'{url}/{file_name}', "w", "utf-8-sig") as custom_file:
            custom_file.write(text)
            custom_file.close
    except:
        pass

def create_custom_folder(folder_name, url):
    """
        folder_name: The name of the folder you want to create.
        url: The path where the folder will be created in.
        To create a folder called 'Travel' on desktop, the url must point to desktop
    """
    try:
        custom_folder = f'{url}/{folder_name}'
        os.mkdir(custom_folder)
    except:
        pass
### FUNCTIONS ###