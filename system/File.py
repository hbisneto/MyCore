import APPINFO

AI_MAJOR = APPINFO.MAJOR_VERSION
AI_MINOR = APPINFO.MINOR_VERSION
AI_BUILD = APPINFO.BUILD_VERSION

VER_DICT = {
    "current" : ["{MajorVersion}", "{MinorVersion}", "{BuildVersion}", "{CurrentVersion}"],
    "target" : ["{TargetMajor}", "{TargetMinor}", "{TargetBuild}", "{TargetVersion}"]
}

appFile = """
### This is the App file
### Here is where you'll start
"""
gitignoreFile = """
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
initFile = """
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
exceptionsFile = """'''
### Exceptions.py

- This file contains events raised when the program must to stop:

```
from exception import Exceptions

def main():
  Exceptions.Throw.FileExists()
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
requirementsFile = f"""'''
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
   TargetMajor = {AI_MAJOR}
   TargetMinor = {AI_MINOR}
   TargetBuild = {AI_BUILD}
   TargetVersion = f'{VER_DICT["target"][0]}.{VER_DICT["target"][1]}.{VER_DICT["target"][2]}'
   ## Target System

   ## Current System
   MajorVersion = sys.version_info[0]
   MinorVersion = sys.version_info[1]
   BuildVersion = sys.version_info[2]
   CurrentVersion = f'{VER_DICT["current"][0]}.{VER_DICT["current"][1]}.{VER_DICT["current"][2]}'
   ## Current System

   ## Uncomment to see information about your system
   ## print(f'>> My system current version: Python {VER_DICT["current"][3]}')
   ## print(f'>> Required version to run: Python {VER_DICT["target"][3]}')

   def CheckVersion():
      if TargetMajor < MajorVersion:
         Exceptions.Throw.MinorVersion(CurrentVersion, TargetVersion, TargetMinor)
      elif TargetMajor > MajorVersion:
         Exceptions.Throw.MajorVersion(CurrentVersion, TargetVersion, MajorVersion)
      else:
         if TargetMinor < MinorVersion:
            Exceptions.Throw.MinorVersion(CurrentVersion, TargetVersion, TargetMinor)
         elif TargetMinor > MinorVersion:
            Exceptions.Throw.MajorVersion(CurrentVersion, TargetVersion, MajorVersion)
         else:
            if TargetBuild < BuildVersion:
               Exceptions.Throw.MinorVersion(CurrentVersion, TargetVersion, TargetMinor)
            elif TargetBuild > BuildVersion:
               Exceptions.Throw.MajorVersion(CurrentVersion, TargetVersion, MajorVersion)
"""
jupyterFile = '''
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## External Packages",    "Packages to set before you go",    "<br>Uncomment the code below to install dependencies"   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# %pip install pandas",    "# %pip install numpy",    "# %pip install qgrid",
    "# %pip install matplotlib",    "# %pip install seaborn"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Check PyBridge Libraries",    "Required libraries will be imported before you run your Jupyter Notebook"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "try:",    "   ## Imported Libraries",    "   from sys import platform",    "",    "   ## Local Libraries",    "   from exception import Exceptions",    "except:",    "   raise RuntimeError('>> Could not import library: Check if the libraries are installed and run the program again.')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Linux Imports",
    "Imports to use in Linux Environments"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Linux",
    "if platform == 'linux' or platform == 'linux2':",
    "   from linux import FileSystem"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## macOS Imports",
    "Imports to use in macOS Environments"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Mac",
    "if platform == 'darwin':",
    "   from mac import FileSystem"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Windows Imports",    "Imports to use in Windows Environments"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Windows",
    "if platform == 'win32' or platform == 'win64':",
    "   from windows import FileSystem"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Code Implementation",
    "Here you will implement your code to be executed after imports"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Examples to make your journey easier",
    "## Note: Replace the code below with your implementation",
    "",
    "# Get the path of your Desktop folder:",
    "print('{0}{1}'.format('Your Desktop Folder: ', FileSystem.Desktop))",
    "",
    "# Get the path of your Documents folder:",
    "print(f'Your Documents Folder: {FileSystem.Documents}')",
    "",
    "# Hello World!",
    "print('Hello World!')",
    "",
    "# Math Sum",
    "print('>> 2 + 3 =', 2 + 3)",
    "",
    "# Throw an Exception using native library",
    "Exceptions.Throw.FileExists()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#",
    "",
    "Copyright © 2023 Heitor. All rights reserved."
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
   "version": "3.10.5"
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
tokensFile = """
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

## Authorization
Auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
Auth.set_access_token(AccessToken, AccessTokenSecret)

## Create an API Object
Twitter = tweepy.API(Auth, wait_on_rate_limit = True)
"""
linuxlib = """
### This is a linux lib file. 

print("Hello, Linux")
"""
maclib = """
'''
### Mac.py

- This file is used to implement code used to run scripts for Mac
- Codes implemented here, will run before the main script starts running
'''
## Mac File
## This file is used to implement code used to run scripts for Mac
## Codes implemented here, will run before the main script starts running

import App
import FileSystem
from system import Requirements
import APPINFO

def Mac():
   ## NOTE: You can use this function
   ## To load information before the app starts running

   ## Lets get Application Info (APPINFO.py)
   APPINFO.loadSplashScreen()

   ## Lets check system requirements
   Requirements.CheckVersion()

   ### You just need to run ONCE: Be sure you commented this code after first run
   # Requirements.InstallDependencies()
   ### You just need to run ONCE: Be sure you commented this code after first run

   ### Verify environment folders
   FileSystem.requiredFolders()

   ## Start App for Mac
   App.start()
"""
windowslib = """
### This is a windows lib file. 

print("Hello, Windows")
"""

