import APPINFO
import codecs
import getpass
import os
import subprocess
import sys
import time
import FileSystem
from datetime import datetime
from exception import Exceptions
from system import File

ProjectType = "Default Project"
AppLocation = ""
ProjectOption = 0

TweetStr = "{Tweet}"

def CreateExceptionsFile(FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as Exceptions:
        Exceptions.write(File.exceptionsFile)
        Exceptions.close()
    print(f'[ O.K ]: Created exceptions Library')

def CreateGitIgnoreFile(FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as GitIgnore:
        GitIgnore.write(File.gitignoreFile)
        GitIgnore.close()
    print(f'[ O.K ]: Created ".gitignore" File')

def CreateInitFile(FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as initFile:
        initFile.write(File.initFile)
        initFile.close()

def CreateJupyterNotebook(FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as JupyterFile:
        JupyterFile.write(File.jupyterFile)
        JupyterFile.close()
    print(f'[ O.K ]: Applied Jupyter Notebook on Environment')

def CreateReadmeFile(AppName, FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as Readme:
        Readme.write('---\n')
        Readme.write(f'This project was created using [PyBridge](https://github.com/hbisneto/PyBridge)\n')
        Readme.write('\n')
        Readme.write('---\n\n')
        Readme.write(f'# {AppName}\n\n')
        Readme.write(f'## Requirements\n\n')
        Readme.write(f'{AppName} requires Python {APPINFO.MAJOR_VERSION}.{APPINFO.MINOR_VERSION}.{APPINFO.BUILD_VERSION} or later to run\n\n')
        Readme.write(f'## Installation\n\n')
        Readme.write(f'```\n')
        Readme.write(f'pip install {AppName}\n')
        Readme.write(f'```\n\n')
        Readme.write(f'## External Links\n\n')
        Readme.write(f'Here is some external links that you can use in your `README.md` file.\n\n')
        Readme.write(f'- [First Link](https://google.com)\n')
        Readme.write(f'- [Second Link](https://google.com)\n')
        Readme.write(f'- [Third Link](https://google.com)\n\n')
        Readme.write(f'#\n\n')
        Readme.write(f'Copyright © {datetime.now().year} {getpass.getuser().capitalize()}. All rights reserved.')
    print(f'[ O.K ]: Created "README" File')

def CreateRequirementsFile(FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as Requirements:
        Requirements.write(File.requirementsFile)
        Requirements.close()
    print(f'[ O.K ]: Created Requirements Library')

def CreateTwitterFile(FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as Tokens:
        Tokens.write(File.tokensFile)
        Tokens.close()
    print(f'[ O.K ]: Applied Twitter Application on Environment')

## Linux File
def CreateLinuxFile(FileLocation):
    print("="*80)
    print(">> Creating Linux Module <<")
    print("="*80)
    with codecs.open(FileLocation, "w", "utf-8-sig") as LinuxFile:
        LinuxFile.write(File.linuxlib)
        LinuxFile.close()
    print(f'[ O.K ]: Created Linux Library')

## Mac File
def CreateMacFile(FileLocation):
    print("="*80)
    print(">> Creating Mac Module <<")
    print("="*80)
    with codecs.open(FileLocation, "w", "utf-8-sig") as MacFile:
        MacFile.write(File.maclib)
        MacFile.close()
    print("[ O.K ]: Created Mac Library")

## Windows File
def CreateWindowsFile(FileLocation):
    print("="*80)
    print(">> Creating Windows Module <<")
    print("="*80)
    with codecs.open(FileLocation, "w", "utf-8-sig") as WindowsFile:
        WindowsFile.write(File.windowslib)
        WindowsFile.close()
    print("[ O.K ]: Created Windows Library")

### TARGET OS MODULES ###

def CreateBridge(projOpt, title):
    print("="*80)
    print(">> CREATE PROJECT <<")
    print("="*80)
    # print(f'>> {ProjectType} <<')
    print(f'>> {title} <<')
    print("="*80)
    UserInput = str(input(">>[!] Project Name: "))
    print(f'>> Creating bridge to the project "{UserInput}"...')
    print("="*80)
    print()
    
    try:
        AppLocation = f'{FileSystem.Repository}{UserInput}'
        os.mkdir(AppLocation)
        AppName = UserInput
    except:
        print()
        print("="*80)
        print(">> Could not create your project:")
        print(f'> Check if "{UserInput}" already exists and try again.')
        print("="*80)
        Exceptions.Throw.ProjectExists()

    # print("CreateEnvironmentTag")
    # print(f'Project Name: {AppName}')
    # print(f'Folder Location: {AppLocation}')

    ### GENERATE MODULES FOR THE BRIDGE
    systemPath = f'{AppLocation}/system'
    exceptionPath = f'{AppLocation}/exception'
    linuxPath = f'{AppLocation}/linux'
    macPath = f'{AppLocation}/mac'
    windowsPath = f'{AppLocation}/windows'

    print("=" * 80)
    print(f'>> Creating {AppName} Modules <<')
    print("=" * 80)
    try:
        os.mkdir(systemPath)
        print(f'[ O.K ]: Created "system" Module')
    except:
        print(f'[ERROR]: The Module "system" could not be created.\n>> Your app may not run.')

    try:
        os.mkdir(exceptionPath)
        print(f'[ O.K ]: Created "exception" Module')
    except:
        print(f'[ERROR]: The Module "exception" could not be created.\n>> Your app may not run.')
    
    try:
        os.mkdir(linuxPath)
        print(f'[ O.K ]: Created "linux" Module')
    except:
        print(f'[ERROR]: The Module "linux" could not be created.\n>> Your app may not run on Linux.')
    
    try:
        os.mkdir(macPath)
        print(f'[ O.K ]: Created "mac" Module')
    except:
        print(f'[ERROR]: The Module "mac" could not be created.\n>> Your app may not run on macOS.')
    
    try:
        os.mkdir(windowsPath)
        print(f'[ O.K ]: Created "windows" Module')
    except:
        print(f'[ERROR]: The Module "windows" could not be created.\n>> Your app may not run on Windows.')
    ### GENERATE MODULES FOR THE BRIDGE

    ### GENERATE LIBRARIES FOR THE BRIDGE
    ## Root Files
    gitignoreFile = f'{AppLocation}/.gitignore'
    initFile = f'{AppLocation}/__init__.py'
    jupyterFile = f'{AppLocation}/{AppName}.ipynb'
    readmeFile = f'{AppLocation}/README.md'
    twitterFile = f'{AppLocation}/Twitter.py'
    ## Root Files

    ## System and Exceptions Files
    exceptionsFile = f'{exceptionPath}/Exceptions.py'
    requirementsFile = f'{systemPath}/Requirements.py'
    ## System and Exceptions Files

    ## Linux Files
    linuxFile = f'{linuxPath}/Linux.py'
    ## Linux Files

    ## Mac Files
    macFile = f'{macPath}/Mac.py'
    ## Mac Files

    ## Windows Files
    windowsFile = f'{windowsPath}/Windows.py'
    ## Windows Files
    ### GENERATE LIBRARIES FOR THE BRIDGE

    ### CRETE BRIDGE
    print("=" * 80)
    print(f'>> Creating {AppName} Libraries and Files <<')
    print("=" * 80)
    CreateExceptionsFile(exceptionsFile)
    CreateGitIgnoreFile(gitignoreFile)
    CreateReadmeFile(AppName, readmeFile)
    CreateRequirementsFile(requirementsFile)

    startTime = time.time()
    if projOpt == 1:
        CreateInitFile(initFile) ## Hbisneto
        CreateLinuxFile(linuxFile)
        CreateMacFile(macFile)
        CreateWindowsFile(windowsFile)
    elif projOpt == 2:
        CreateInitFile(initFile)
        CreateLinuxFile(linuxFile)
        CreateMacFile(macFile)
        CreateWindowsFile(windowsFile)
    elif projOpt == 3:
        CreateInitFile(initFile)
        CreateTwitterFile(twitterFile)
        CreateLinuxFile(linuxFile)
        CreateMacFile(macFile)
        CreateWindowsFile(windowsFile)
    elif projOpt == 4:
        CreateJupyterNotebook(jupyterFile)

    print("="*80)
    endTime = time.time()
    timeTaken = endTime-startTime

    if timeTaken < 1:
        print(f'[ DONE ]: The bridge to the project "{AppName}" was created in less than a second')
    else:
        print(f'[ DONE ]: The bridge to the project "{AppName}" was created in {timeTaken:.2f}')
    print("="*80)
    print()

    ### OPEN PROJECT FOLDER
        # cmd = subprocess.getoutput(f'open {AppLocation}')

        # userInput = str(input(">> Would you like to open project in Visual Studio Code? [Y/n]: "))

        # if userInput == "Y" or userInput == "y":
        #     cmd = subprocess.getoutput(f'cd {AppLocation}')
        #     cmd = subprocess.getoutput(f'code .')
    ### OPEN PROJECT FOLDER

    ### CRETE BRIDGE
    
    ### BRIDGE CREATION OPTIONS
    # CreateExceptionsFile(AppName, exceptionsFile)
    # CreateGitIgnoreFile(AppName, gitignoreFile)
    # CreateInitFile(AppName, initFile)
    # CreateJupyterNotebook(AppName, jupyterFile)
    # CreateReadmeFile(AppName, readmeFile)
    # CreateRequirementsFile(AppName, requirementsFile)
    # CreateTokensFile(AppName, tokensFile)

    # CreateLinuxAppFile(AppName, linuxAppFile)
    # CreateLinuxFile(AppName, linuxFile)
    # CreateLinuxFileSystem(AppName, linuxFSFile)
    # CreateLinuxSplashScreen(AppName, splashLinuxFile)
    
    # CreateMacAppFile(AppName, macAppFile)
    # CreateMacFile(AppName, macFile)
    # CreateMacFileSystem(AppName, macFSFile)
    # CreateMacSplashScreen(AppName, splashMacFile)
    
    # CreateWindowsAppFile(AppName, windowsAppFile)
    # CreateWindowsFile(AppName, windowsFile)
    # CreateWindowsFileSystem(AppName, windowsFSFile)
    # CreateWindowsSplashScreen(AppName, splashWindowsFile)
    ### BRIDGE CREATION OPTIONS