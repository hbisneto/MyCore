import info
import cli
import codecs
import os
import time
import filesystem as fs
from datetime import datetime
from exceptions import exception
from filesystem import wrapper as wr
from system import menus

# ProjectType = "Default Project"
# AppLocation = ""
# ProjectOption = 0

tweet_string = "{tweet}"
repository_folder = f'{fs.documents}/{info.NAME}/Repository'

# list_projects = []
backup_folder = f'{fs.CURRENT_LOCATION}/Backup'







### FUNCTIONS ###


# def create_backup_folder():
#     """Creates the 'Backup' folder in the root of the project
#     """
#     try:
#         os.mkdir(backup_folder)
#     except:
#         pass
### FUNCTIONS ###












LIST_MENU_ITEMS = [
    "New Project",
    "Project List",
    "Backup Projects",
    "Sample Projects"
]

LIST_PROJECTS = [
    "Create Blank Project",
    "Create a Menu Application",
    "Create a Twitter Application",
    "Create a Jupyter Notebook"
]

LIST_PROJECT_OPTIONS = {
    0:[
        "Create Library", 
        "Will add a Library in all OS Modules"
      ],
    1:[
        "Create Universal Library",
        "Will add a new Library on the root of project"
      ],
    2:[
        "Create Module",
        "Will add a Module in all OS Modules"
      ],
    3:[
        "Create Universal Module",
        "Will add a new Module on the root of project"
      ],
    4:[
        "Delete Project",
        "Deletes the project folder and all the contents in it. \nCAUTION: THIS OPERATION CANNOT BE UNDONE!"
      ]
}

def get_project_list(repository):
    ### List projects PyBridge creates
    cli.make_menu("PROJECT LIST", style = "default", new_line = True)
    count = 0
    for dir in os.listdir(repository):
        if os.path.isdir(os.path.join(repository, dir)):
            count+=1
            print(f'[{count}]: {dir}')

    if count == 0:
      cli.make_menu(f'>> It`s lonely here', 'Your list of projects is empty', style="short", new_line=True)
    # else:
    #   pass
      # opc = int(input(">> Type a number to get an option or go back: "))
      # if opc != 0:### PENSAR NESSA PARTE
      #   menus.menu_project_options()
    cli.separator()

def generate_modules(bridge_name, bridge_location):
  BRIDGE_FOLDERS = {
    0: "exceptions",
    1: "system",
    2: "linux",
    3: "mac",
    4: "windows"
  }
  ### GENERATE MODULES FOR THE BRIDGE
  cli.make_menu(f'>> Creating {bridge_name} Modules')
  try:
    for i in BRIDGE_FOLDERS:
      wr.create_directory(f'{bridge_location}/{BRIDGE_FOLDERS[i]}')
      print(f'[ O.K ]: Created "{BRIDGE_FOLDERS[i]}" Module')
    cli.separator()
  except:
    print(f'[ERROR]: The Module "{BRIDGE_FOLDERS[i]}" could not be created.\n>> Your app may not run.')
  ### GENERATE MODULES FOR THE BRIDGE

def create_app_file(proj_opt, bridge_name, file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    if proj_opt == 1:
      file = f"""
### This is the App file
# Here is where you'll start

def start():
  print("Hello World")
"""
    elif proj_opt == 2:
      file = f"""
## {bridge_name} File
## This file is used to implement code used to run application in loop

from exceptions import exception

def start():
  while True:
    print("="*80)
    print(">> Options Menu <<")
    print(">> 1. Option One")
    print(">> 2. Option Two")
    print(">> 3. Option Three")

    try:
        user_input = int(input(">>[!] Type the option number: "))
        print("="*80)
        if user_input == 1:
          print("> Option 1")
        elif user_input == 2:
          print("> Option 2")
        elif user_input == 3:
          print("> Option 3")
        else:
          print(">> This option is unavailable at this time")
    except:
        print("-"*80)
        print(">> This option is not available")
        print("-"*80)

start()
"""    
    elif proj_opt == 3:
      file = f"""
## MacApp File
## This file is used to implement code used to run scripts for Mac

import tokens
from exceptions import exception

def start():
  print("="*80)
  print("NEW TWEET")
  print("="*80)
  tweet = str(input(">>[!] Whats happening? "))
  print("="*80)
  print()
  print("-"*80)
  print(">> Your tweet was sent")
  print("-"*80)
  print()
  print("="*80)

  try:
    tokens.twitter.update_status(tweet)
    print(f'>> Your last tweet:')
    print(f' > {tweet_string}')
    print("-" * 80)
  except:
    print(">>  Something went wrong: Unabled to connect to Twitter.")

start()
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "app" Library')

def create_exception_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file = """'''
### exception.py

- This file contains events raised when the program must to stop:

```
from exception import Exceptions

def main():
  exceptions.Throw.FileExists()
```
Output:

```
Traceback (most recent call last):
  File "/YourProject/mac/MacApp.py", line 11, in Main
    Exceptions.Throw.FileExists()
  File "/YourProject/exception/Exceptions.py", line 53, in FileExists
    raise Exception(f'{self.exctype} The file already exists')
Exception: >> An Exception occurred: The file already exists
```
'''
## Exceptions File
## This file contains events that's raised when the program must to stop

class Raise:
  def MajorVersion(self, CurrentVersion, TargetVersion, TargetMajor):
    raise Exception(f'>> You cannot run the application because it requires Python {TargetVersion} or later. [Current Version: {CurrentVersion}]')

  def MinorVersion(self, CurrentVersion, TargetVersion, TargetMinor):
    print('=' * 80)
    print(">> PYBRIDGE <<")
    print('=' * 80)
    print(">> WARNING <<")
    print('=' * 80)
    print(f'>> Your appication targets a version of Python older than the version currently')
    print('installed. You may get errors during the process')
    print('=' * 80)
    print(f'- Current Version: {CurrentVersion}')
    print(f'- Target Version: {TargetVersion}')
    print(f'>> You can change `Requirements.py` on `system` Module')
    print('=' * 80)
    print()

  def BuildVersion(self, CurrentVersion, TargetVersion, BuildVer):
    raise Exception(f'>> This application can only run on Python {TargetVersion}. [Current Version: {CurrentVersion}]')

  def __init__(self, exctype):
    self.exctype = exctype

  def FileExists(self):
    raise Exception(f'{self.exctype} The file already exists')
  
  def DirectoryExists(self):
    raise Exception(f'{self.exctype} The directory already exists')
  
  def ProjectExists(self):
    raise Exception(f'{self.exctype} The project already exists')
  
  def ImportLib(self):
    raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")

  def InputFormat(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} INVALID INPUT')
    print("=" * 80)
    print(">> Your input is not valid: Check your input and try again")
    print("=" * 80)
  
  def ProgramQuit(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} PYBRIDGE HAS QUIT!')
    print("=" * 80)
    print(f'>> The program has been closed and couldn`t be restored.')
    print('>> Run the program again!')
    print("=" * 80)

  def InvalidOption(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} INVALID OPTION')
    print("=" * 80)
    print(f'>> You typed an invalid option.')
    print("=" * 80)

  def ProjectsLoadFail(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} PROJECT LOADING FAILED!')
    print("=" * 80)
    print(f'>> ERROR: Couldn`t load projects...')
    print("=" * 80)

  def BackupFail(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} BACKUP CREATION FAILED!')
    print("=" * 80)
    print("*" * 80)
    print(f'>> PyBridge could not create backup for your projects folder')
    print(f'>> Try again later.')
    print("*" * 80)

  def CompressBackupFail(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} COMPRESSED FILE CREATION FAILED!')
    print("=" * 80)
    print("*" * 80)
    print(f'>> PyBridge could not create a compressed file from your backup')
    print(f'>> Try again later.')
    print("*" * 80)

Throw = Raise("")
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "exception" Library')

def create_filesystem_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file = """
'''
filesystem.py

- This file contains some default directories of your system
- You can use this file to implement custom directories used by your application
'''
## FileSystem
## This file contains some default directories of your system
## You can use this file to implement custom directories used by your application

### NATIVE LIBRARIES ###
import os
import codecs
from sys import platform
### NATIVE LIBRARIES ###

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
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "filesystem" Library')

def create_info_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file ="""
'''
### Info.py

- This file contains information about your project
'''

import getpass
import sys
from datetime import date
from datetime import datetime
from sys import platform

NAME = "MyCore"
VERSION = "1.9"
COPYRIGHT = "Heitor Bisneto"
TYPE = "Menu Application Loop"
LICENCE = "MIT"
USERNAME_CURRENT = getpass.getuser().capitalize()

### Python running version
MAJOR_VERSION = sys.version_info[0]
MINOR_VERSION = sys.version_info[1]
BUILD_VERSION = sys.version_info[2]
CURRENT_PYTHON_VERSION = f'{MAJOR_VERSION}.{MINOR_VERSION}.{BUILD_VERSION}'
### Python running version

CURRENT_YEAR = date.today().year
NOW = datetime.now()
HOUR = int(NOW.strftime("%H"))
TIME_ACCESS = NOW.strftime("%H:%M:%S")

### UNCOMMENT TO USE VARIABLES
# Minute = int(Now.strftime("%M"))
# Second = int(Now.strftime("%S"))
### UNCOMMENT TO USE VARIABLES
        
def loadSplashScreen():
    print("="*80)
    print(f'[{NAME} for {PLATFORM_NAME}] - Running...')
    print("="*80)

    print(f'Name: {NAME}')
    print(f'Version: {VERSION}')
    print(f'Created By: {COPYRIGHT}')

    if CURRENT_YEAR == 2021:
        print(f'Copyright © {CURRENT_YEAR} | {COPYRIGHT}. All rights reserved.')
        print("="*80)
    else:
        print(f'Copyright © 2021 - {CURRENT_YEAR} | {COPYRIGHT}. All rights reserved.')
        print("="*80)

    if HOUR >= 6 and HOUR < 12:
        DAY_PERIOD = "Morning"
        print(f'Hello {USERNAME_CURRENT}. Good {DAY_PERIOD}! - {TIME_ACCESS}')
        print("="*80)
    elif HOUR >= 12 and HOUR < 18:
        DAY_PERIOD = "Afternoon"
        print(f'Hello {USERNAME_CURRENT}. Good {DAY_PERIOD}! - {TIME_ACCESS}')
        print("="*80)
    elif HOUR >= 18 and HOUR != 0:
        DAY_PERIOD = "Evening"
        print(f'Hello {USERNAME_CURRENT}. Good {DAY_PERIOD}! - {TIME_ACCESS}')
        print("="*80)
    else:
        print(f'Hello {USERNAME_CURRENT}. Nice to see you! - {TIME_ACCESS}')
        print("="*80)

## Linux
if platform == "linux" or platform == "linux2":
    PLATFORM_NAME = "Linux"
## Mac
elif platform == "darwin":
    PLATFORM_NAME = "Mac"
## Windows
elif platform == "win32" or platform == "win64":
    PLATFORM_NAME = "Windows"

# print(NAME)
# print(VERSION)
# print(COPYRIGHT)
# print(TYPE)
# print(LICENCE)
# print(USERNAME_CURRENT)

# print(MAJOR_VERSION)
# print(MINOR_VERSION)
# print(BUILD_VERSION)
# print(CURRENT_PYTHON_VERSION)

# print(CURRENT_YEAR)
# print(NOW)
# print(HOUR)
# print(TIME_ACCESS)
# print(PLATFORM_NAME)
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "info" Library')

def create_linux_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file = """
### This is a linux lib file. 

print("Hello, Linux")
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "linux" Library')

def create_mac_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file = """
'''
### Mac.py

- This file is used to implement code used to run scripts for Mac
- Codes implemented here, will run before the main script starts running
'''
## Mac File
## This file is used to implement code used to run scripts for Mac
## Codes implemented here, will run before the main script starts running

import app
import info
from system import filesystem as fs
from system import requirements as req

def mac():
  ## NOTE: You can use this function
  ## To load information before the app starts running

  ## Lets get Application Info (info.py)
  info.loadSplashScreen()

  ## Lets check system requirements
  req.check_version()

  ## Start App for Mac
  app.start()
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "mac" Library')

def create_windows_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    file = """
### This is a windows lib file. 

print("Hello, Windows")
"""
    writer.write(file)
    writer.close()
  print(f'[ O.K ]: Created "windows" Library')

def create_readme_file(bridge_name, file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
    readmelib = f"""
---
This project was created using [PyBridge](https://github.com/hbisneto/PyBridge)

---

# {bridge_name}

## Requirements

{bridge_name} requires Python  or later to run

## Installation

```
pip install {bridge_name}
```

## External Links

Here is some external links that you can use in your `README.md` file.

- [First Link](https://google.com)
- [Second Link](https://google.com)
- [Third Link](https://google.com)

#

Copyright © {info.CURRENT_YEAR} {info.USERNAME_CURRENT}. All rights reserved.
"""
    writer.write(readmelib)
    writer.close()
  print(f'[ O.K ]: Created "README" Markdown')

def create_twitter_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
      file = """
## Tokens
## Setup and connect you Twitter account here!
# Note: DO NOT share your tokens
## You can generate and regenerate tokens on Twitter Developer Platform

import tweepy
from tweepy import OAuthHandler

## API Key and API Key Secret
ConsumerKey = str('')
ConsumerSecret = str('')

## Access Token and Access Token Secret
AccessToken = str("")
AccessTokenSecret = str("")

## Authorisation
Auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
Auth.set_access_token(AccessToken, AccessTokenSecret)

## Create an API Object
Twitter = tweepy.API(Auth, wait_on_rate_limit = True)
"""
      writer.write(file)
      writer.close()
  print(f'[ O.K ]: Created "twitter" Library (tokens for Twitter)')

def create_requirements_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
      VER_DICT = {
          "current" : ["{current_major}", "{current_minor}", "{current_build}", "{current_version}"],
          "target" : ["{target_major}", "{target_minor}", "{target_build}", "{target_version}"]
      }
      file = f"""'''
### Requirements.py

- This file is used to check if system matches with the minimum requirements to run
'''

## Requirements File
## This file is used to check if system matches with the minimum requirements to run

import sys
import subprocess
from exception import Exceptions

## Change "REQUIRE" to "False" to skip system check
REQUIRE = True
## Change "REQUIRE" to "True" to allow system check

if REQUIRE == True:
## Target System
target_major = {info.MAJOR_VERSION}
target_minor = {info.MINOR_VERSION}
target_build = {info.BUILD_VERSION}
target_version = f'{VER_DICT["target"][0]}.{VER_DICT["target"][1]}.{VER_DICT["target"][2]}'

target_ver_str = f'{VER_DICT["target"][0]}{VER_DICT["target"][1]}{VER_DICT["target"][2]}'
target_ver_int = int(target_ver_str)
## Target System

## Current System
current_major = sys.version_info[0]
current_minor = sys.version_info[1]
current_build = sys.version_info[2]
current_version = f'{VER_DICT["current"][0]}.{VER_DICT["current"][1]}.{VER_DICT["current"][2]}'
current_ver_str = f'{VER_DICT["current"][0]}{VER_DICT["current"][1]}{VER_DICT["current"][2]}'
current_ver_int = int(current_ver_str)
## Current System

## Uncomment to see information about your system
## print(f'>> My system current version: Python {VER_DICT["current"][3]}')
## print(f'>> Required version to run: Python {VER_DICT["target"][3]}')

def check_version():
  if target_ver_int < current_ver_int:
      Exceptions.Throw.minor_version(current_version, target_version)
  elif target_ver_int > current_ver_int:
      Exceptions.Throw.major_version(current_version, target_version)
  else:
      pass
"""
      writer.write(file)
      writer.close()
  print(f'[ O.K ]: Created "requirements" Library')

def create_gitignore_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
      file = """
### PYBRIDGE SETS TO IGNORE ###
## .DS_Store: Is a file that stores custom attributes of its containing folder,
## such as folder view options, icon positions, and other visual information on macOS
.DS_Store
### PYBRIDGE SETS TO IGNORE ###

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
"""
      writer.write(file)
      writer.close()
  print(f'[ O.K ]: Created ".gitignore" file')

def create_init_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
      file = """
## __init__.py File
## This file is used to first run your application
## Here the contents will be processed to choose the best platform to go

## Native Libraries
from sys import platform

## Linux
if platform == "linux" or platform == "linux2":
  # from linux import Linux
  # Linux.Linux()
  print("=" * 80)
  print("[!] THIS SOFTWARE IS NOT COMPATIBLE WITH THIS PLATFORM")
  print("=" * 80)

## Mac
elif platform == "darwin":
  from mac import Mac
  Mac.Mac()
  
## Windows
elif platform == "win32" or platform == "win64":
  # from windows import Windows
  # Windows.Windows()
  print("=" * 80)
  print("[!] THIS SOFTWARE IS NOT COMPATIBLE WITH THIS PLATFORM")
  print("=" * 80)
"""
      writer.write(file)
      writer.close()
  print(f'[ O.K ]: Created "__init__" file')

def create_jupyter_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
      file = '''
{
"cells": [
{
  "cell_type": "markdown",
  "metadata": {},
  "source": [
  "## External Packages\n",
  "Packages to set before you go\n",
  "<br>Uncomment the code below to install dependencies"
  ]
},
{
  "cell_type": "code",
  "execution_count": null,
  "metadata": {},
  "outputs": [],
  "source": [
  "# %pip install pandas\n",
  "# %pip install numpy\n",
  "# %pip install qgrid\n",
  "# %pip install matplotlib\n",
  "# %pip install seaborn\n",
  "from system import filesystem as fs\n",
  "from exceptions import exception"
  ]
},
{
  "cell_type": "markdown",
  "metadata": {},
  "source": [
  "## Check PyBridge Libraries\n",
  "Required libraries will be imported before you run your Jupyter Notebook"
  ]
},
{
  "cell_type": "code",
  "execution_count": null,
  "metadata": {},
  "outputs": [],
  "source": [
  "# from system import filesystem as fs\n",
  "# from exceptions import exception"
  ]
},
{
  "cell_type": "markdown",
  "metadata": {},
  "source": [
  "# Code Implementation\n",
  "Here you will implement your code to be executed after imports"
  ]
},
{
  "cell_type": "code",
  "execution_count": null,
  "metadata": {},
  "outputs": [],
  "source": [
  "## Examples to make your journey easier\n",
  "## Note: Replace the code below with your implementation\n",
  "\n",
  "# Get the path of your Desktop folder:\n",
  "print('{0}{1}'.format('Your Desktop Folder: ', fs.desktop))\n",
  "\n",
  "# Get the path of your Documents folder:\n",
  "print(f'Your Documents Folder: {fs.documents}')\n",
  "\n",
  "# Hello World!\n",
  "print('Hello World!')\n",
  "\n",
  "# Math Sum\n",
  "print('>> 2 + 3 =', 2 + 3)\n",
  "\n",
  "# Throw an Exception using native library\n",
  "exception.Throw.file_exists()"
  ]
},
{
  "cell_type": "markdown",
  "metadata": {},
  "source": [
  "#\n",
  "\n",
  "This project was created using PyBridge. All rights reserved."
  ]
}
],
"metadata": {
"kernelspec": {
  "display_name": "Python 3.9.0 64-bit",
  "language": "python",
  "name": "python3"
},
"language_info": {
  "codemirror_mode": {
  "name": "ipython",
  "version": 3
  },
  "file_extension": ".py",
  "mimetype": "text/x-python",
  "name": "python",
  "nbconvert_exporter": "python",
  "pygments_lexer": "ipython3",
  "version": "3.9.0"
},
"orig_nbformat": 4,
"vscode": {
  "interpreter": {
  "hash": "aee8b7b246df8f9039afb4144a1f6fd8d2ca17a180786b69acc140d282b71a49"
  }
}
},
"nbformat": 4,
"nbformat_minor": 2
}
'''
      writer.write(file)
      writer.close()
  print(f'[ O.K ]: Created "Jupyter Notebook" file')

def create_logs_file(file_location):
  with codecs.open(file_location, "w", "utf-8-sig") as writer:
      file = """
### This is a Logs lib file. 

print("Hello, Windows")
"""
      writer.write(file)
      writer.close()
  print(f'[ O.K ]: Created "logs" Library')

def create(proj_opt, title):
  cli.make_menu("CREATE PROJECT")
  print(f'>> {title} <<')
  cli.separator()
  bridge_name = str(input(">>[!] Project Name: "))

  ## Root Files
  bridge_app_file = f'{repository_folder}/{bridge_name}/{bridge_name}.py'
  bridge_gitignore_file = f'{repository_folder}/{bridge_name}/.gitignore'
  bridge_info_file = f'{repository_folder}/{bridge_name}/info.py'
  bridge_init_file = f'{repository_folder}/{bridge_name}/__init__.py'
  bridge_jupyter_file = f'{repository_folder}/{bridge_name}/{bridge_name}.ipynb'
  bridge_twitter_file = f'{repository_folder}/{bridge_name}twitter.py'
  bridge_readme_file = f'{repository_folder}/{bridge_name}/README.md'
  ## Root Files

  # Nested Files
  bridge_exception_file = f'{repository_folder}/{bridge_name}/exceptions/exception.py'
  bridge_linux_file = f'{repository_folder}/{bridge_name}/linux/linux.py'
  bridge_mac_file = f'{repository_folder}/{bridge_name}/mac/mac.py'
  bridge_windows_file = f'{repository_folder}/{bridge_name}/windows/windows.py'
  bridge_filesystem_file = f'{repository_folder}/{bridge_name}/system/filesystem.py'
  bridge_logs_file = f'{repository_folder}/{bridge_name}/system/logs.py'
  bridge_requirements_file = f'{repository_folder}/{bridge_name}/system/requirements.py'
  # Nested Files

  # print(f'>> Creating bridge to the project "{bridge_name}"...')
  # print("="*80)

  cli.make_menu(f'>> Creating bridge to the project "{bridge_name}"...')

  try:
    bridge_location = f'{repository_folder}/{bridge_name}/'
    os.mkdir(bridge_location)
  except:
    print()
    print("="*80)
    print(">> Could not create your project:")
    print(f'> Check if "{bridge_name}" already exists and try again.')
    print("="*80)
    exception.Throw.project_exists()

  generate_modules(bridge_name, bridge_location)

  ### CRETE BRIDGE
  cli.make_menu(f'Creating "{bridge_name}" Libraries and Files')

  ### Creates the main files to the bridge
  # Root folder
  # Exceptions folder
  # System folder
  # create_filesystem_file(bridge_filesystem_file)
  ### Creates the main files to the bridge

  start_time = time.time()
  if proj_opt == 1:
    # print("1")
    create_app_file(proj_opt, bridge_name, bridge_app_file)
    create_exception_file(bridge_exception_file)
    create_info_file(bridge_info_file)
    create_init_file(bridge_init_file) # Do not create in case of Jupyter Notebook
    create_gitignore_file(bridge_gitignore_file)
    create_readme_file(bridge_name, bridge_readme_file)
    create_logs_file(bridge_logs_file)
    create_requirements_file(bridge_requirements_file) # Do not create in case of Jupyter Notebook

    create_linux_file(bridge_linux_file)
    create_mac_file(bridge_mac_file)
    create_windows_file(bridge_windows_file)
    # test(bridge_name, readmeFile)

    # CreateInitFile(initFile) ## Hbisneto
    # CreateLinuxFile(linuxFile)
    # CreateMacFile(macFile)
    # CreateWindowsFile(windowsFile)
  elif proj_opt == 2:
    print("2")
    create_app_file(proj_opt, bridge_name, bridge_app_file)
    # CreateInitFile(initFile)
    # CreateLinuxFile(linuxFile)
    # CreateMacFile(macFile)
    # CreateWindowsFile(windowsFile)
  elif proj_opt == 3:
    print("3")
    create_app_file(proj_opt, bridge_name, bridge_app_file)
    create_twitter_file(bridge_twitter_file)
    # CreateInitFile(initFile)
    # CreateTwitterFile(twitterFile)
    # CreateLinuxFile(linuxFile)
    # CreateMacFile(macFile)
    # CreateWindowsFile(windowsFile)
  elif proj_opt == 4:
    create_jupyter_file(bridge_jupyter_file)
    # CreateJupyterNotebook(jupyterFile)

  print("="*80)
  end_time = time.time()
  time_taken = (end_time - start_time)

  if time_taken < 1:
    print(f'[ DONE ]: The bridge to the project "{bridge_name}" was created in less than a second')
    cli.make_menu(text="Algum texto")
  else:
    print(f'[ DONE ]: The bridge to the project "{bridge_name}" was created in {time_taken:.2f}')
    cli.make_menu(text="Algum texto")
  print("="*80)
