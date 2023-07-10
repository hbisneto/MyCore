"""
### Core.py

This is where all the resources of each platform will work.
You can use and customize default functions to fit your work. 

### Functions you can call:

`CreateExceptionsFile()`: This is something.

`CreateGitIgnoreFile()`:

`CreateInitFile()`:

`CreateJupyterNotebook()`:

`CreateReadmeFile()`:

`CreateRequirementsFile()`:

`CreateTwitterFile()`:


#### Linux Functions

`CreateLinuxAppFile()`:

`CreateLinuxFile()`:

`CreateLinuxFileSystem()`:

`CreateLinuxSplashScreen()`:

#### macOS Functions:

`CreateMacAppFile()`:

`CreateMacFile()`:

`CreateMacFileSystem()`:

`CreateMacSplashScreen()`:

#### Windows Functions:

`CreateWindowsAppFile()`:

`CreateWindowsFile()`:

`CreateWindowsFileSystem()`:

`CreateWindowsSplashScreen()`:
"""

import codecs
import getpass
import os
import subprocess
import sys
import time
from datetime import datetime
from exception import Exceptions
from mac import FileSystem

ProjectType = "Default Project"
AppLocation = ""
ProjectOption = 0
MajorVersion = sys.version_info[0]
MinorVersion = sys.version_info[1]
BuildVersion = sys.version_info[2]
TweetStr = "{Tweet}"

def CreateExceptionsFile(AppName, FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as Exceptions:
        Exceptions.write(f'## Exceptions File\n')
        Exceptions.write(f'## This file contains events that`s raised when the program must to stop\n\n')
        Exceptions.write(f'class Raise:\n')
        Exceptions.write(f'  def MajorVersion(self, CurrentVersion, TargetVersion, TargetMajor):\n')
        Exceptions.write("    raise Exception(f'>> You cannot run the application because it requires Python {TargetVersion} or later. [Current Version: {CurrentVersion}]')\n\n")
        Exceptions.write(f'  def MinorVersion(self, CurrentVersion, TargetVersion, TargetMinor):\n')
        Exceptions.write(f"    print('=' * 80)\n")
        Exceptions.write(f'    print(">> PYBRIDGE <<")\n')
        Exceptions.write(f"    print('=' * 80)\n")
        Exceptions.write(f'    print(">> WARNING <<")\n')
        Exceptions.write(f"    print('=' * 80)\n")
        Exceptions.write("    print(f'>> Your appication targets a version of Python older than the version currently installed. You may get errors during the process')\n")
        Exceptions.write(f"    print('=' * 80)\n")
        Exceptions.write("    print(f'- Current Version: {CurrentVersion}')\n")
        Exceptions.write("    print(f'- Target Version: {TargetVersion}')\n")
        Exceptions.write("    print(f'>> You can change `Requirements.py` on `system` Module')\n")
        Exceptions.write(f"    print('=' * 80)\n")
        Exceptions.write(f'    print()\n\n')
        Exceptions.write(f'  def BuildVersion(self, CurrentVersion, TargetVersion, BuildVer):\n')
        Exceptions.write("    raise Exception(f'>> This application only can run on Python {TargetVersion}. [Current Version: {CurrentVersion}]')\n\n")
        Exceptions.write(f'  def __init__(self, exctype):\n')
        Exceptions.write(f'    self.exctype = exctype\n\n')
        Exceptions.write(f'  def FileExists(self):\n')
        Exceptions.write("    raise Exception(f'{self.exctype} The file already exists')\n\n")
        Exceptions.write(f'  def DirectoryExists(self):\n')
        Exceptions.write("    raise Exception(f'{self.exctype} The directory already exists')\n\n")
        Exceptions.write(f'  def ImportLib():\n')
        Exceptions.write(f'   raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")\n\n')
        Exceptions.write(f'  def InputFormat(self):\n')
        Exceptions.write(f'    print("=" * 80)\n')
        Exceptions.write("    print(f'{self.exctype} INVALID INPUT')\n")
        Exceptions.write(f'    print("=" * 80)\n')
        Exceptions.write(f'    print(">> Your input is not valid: Check your input and try again")\n')
        Exceptions.write(f'    print("=" * 80)\n\n')
        Exceptions.write(f'  def ProgramQuit(self):\n')
        Exceptions.write(f'    print("=" * 80)\n')
        Exceptions.write("    print(f'{self.exctype} PYBRIDGE HAS QUIT!')\n")
        Exceptions.write(f'    print("=" * 80)\n')
        Exceptions.write("    print(f'>> The program has been closed and couldn`t be restored.')\n")
        Exceptions.write("    print(f'>> Run the program again!')\n")
        Exceptions.write(f'    print("=" * 80)\n\n')
        Exceptions.write(f'  def InvalidOption(self):\n')
        Exceptions.write(f'    print("=" * 80)\n')
        Exceptions.write("    print(f'{self.exctype} INVALID OPTION')\n")
        Exceptions.write(f'    print("=" * 80)\n')
        Exceptions.write("    print(f'>> You typed an invalid option.')\n")
        Exceptions.write("    print(f'>> Running the program again!')\n")
        Exceptions.write(f'    print("=" * 80)\n\n')
        Exceptions.write(f'  def ProjectsLoadFail(self):\n')
        Exceptions.write(f'    print("=" * 80)\n')
        Exceptions.write("    print(f'{self.exctype} PROJECT LOADING FAILED!')\n")
        Exceptions.write(f'    print("=" * 80)\n')
        Exceptions.write("    print(f'>> ERROR: Couldn`t load projects...')\n")
        Exceptions.write(f'    print("=" * 80)\n\n')
        Exceptions.write(f'  def BackupFail(self):\n')
        Exceptions.write(f'    print("=" * 80)\n')
        Exceptions.write("    print(f'{self.exctype} BACKUP CREATION FAILED!')\n")
        Exceptions.write(f'    print("=" * 80)\n')
        Exceptions.write(f'    print("*" * 80)\n')
        Exceptions.write("    print(f'>> PyBridge could not create backup for your projects folder')\n")
        Exceptions.write("    print(f'>> Try again later.')\n")
        Exceptions.write(f'    print("*" * 80)\n\n')
        Exceptions.write(f'  def CompressBackupFail(self):\n')
        Exceptions.write(f'    print("=" * 80)\n')
        Exceptions.write("    print(f'{self.exctype} COMPRESSED FILE CREATION FAILED!')\n")
        Exceptions.write(f'    print("=" * 80)\n')
        Exceptions.write(f'    print("=" * 80)\n')
        Exceptions.write("    print(f'>> PyBridge could not create a compressed file from your backup')\n")
        Exceptions.write("    print(f'>> Try again later.')\n")
        Exceptions.write(f'    print("=" * 80)\n\n')
        Exceptions.write(f'Throw = Raise(">> An Exception occurred:")')
        Exceptions.close()
    print(f'[ O.K ]: Created exceptions Library')

def CreateGitIgnoreFile(AppName, FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as GitIgnore:
        GitIgnore.write(f'### PYBRIDGE SETS TO IGNORE ###\n')
        GitIgnore.write(f'## .DS_Store: Is a file that stores custom attributes of its containing folder, such as folder view options, icon positions, and other visual information.\n')
        GitIgnore.write(f'.DS_Store\n')
        GitIgnore.write(f'### PYBRIDGE SETS TO IGNORE ###\n\n')
        GitIgnore.write(f'# Byte-compiled / optimized / DLL files\n')
        GitIgnore.write(f'__pycache__/\n')
        GitIgnore.write(f'*.py[cod]\n')
        GitIgnore.write(f'*$py.class\n\n')
        GitIgnore.write(f'# C extensions\n')
        GitIgnore.write(f'*.so\n\n')
        GitIgnore.write(f'# Distribution / packaging\n')
        GitIgnore.write(f'.Python\n')
        GitIgnore.write(f'build/\n')
        GitIgnore.write(f'develop-eggs/\n')
        GitIgnore.write(f'dist/\n')
        GitIgnore.write(f'downloads/\n')
        GitIgnore.write(f'eggs/\n')
        GitIgnore.write(f'.eggs/\n')
        GitIgnore.write(f'lib/\n')
        GitIgnore.write(f'lib64/\n')
        GitIgnore.write(f'parts/\n')
        GitIgnore.write(f'sdist/\n')
        GitIgnore.write(f'var/\n')
        GitIgnore.write(f'wheels/\n')
        GitIgnore.write(f'share/python-wheels/\n')
        GitIgnore.write(f'*.egg-info/\n')
        GitIgnore.write(f'.installed.cfg\n')
        GitIgnore.write(f'*.egg\n')
        GitIgnore.write(f'MANIFEST\n\n')
        GitIgnore.write(f'# PyInstaller\n')
        GitIgnore.write(f'#  Usually these files are written by a python script from a template\n')
        GitIgnore.write(f'#  before PyInstaller builds the exe, so as to inject date/other infos into it.\n')
        GitIgnore.write(f'*.manifest\n')
        GitIgnore.write(f'*.spec\n\n\n')
        GitIgnore.write(f'# Installer logs\n')
        GitIgnore.write(f'pip-log.txt\n')
        GitIgnore.write(f'pip-delete-this-directory.txt\n\n')
        GitIgnore.write(f'# Unit test / coverage reports\n')
        GitIgnore.write(f'htmlcov/\n')
        GitIgnore.write(f'.tox/\n')
        GitIgnore.write(f'.nox/\n')
        GitIgnore.write(f'.coverage\n')
        GitIgnore.write(f'.coverage.*\n')
        GitIgnore.write(f'.cache\n')
        GitIgnore.write(f'nosetests.xml\n')
        GitIgnore.write(f'coverage.xml\n')
        GitIgnore.write(f'*.cover\n')
        GitIgnore.write(f'*.py,cover\n')
        GitIgnore.write(f'.hypothesis/\n')
        GitIgnore.write(f'.pytest_cache/\n')
        GitIgnore.write(f'cover/\n\n')
        GitIgnore.write(f'# Translations\n')
        GitIgnore.write(f'*.mo\n')
        GitIgnore.write(f'*.pot\n\n')
        GitIgnore.write(f'# Django stuff:\n')
        GitIgnore.write(f'*.log\n')
        GitIgnore.write(f'local_settings.py\n')
        GitIgnore.write(f'db.sqlite3\n')
        GitIgnore.write(f'db.sqlite3-journal\n\n')
        GitIgnore.write(f'# Flask stuff:\n')
        GitIgnore.write(f'instance/\n')
        GitIgnore.write(f'.webassets-cache\n\n')
        GitIgnore.write(f'# Scrapy stuff:\n')
        GitIgnore.write(f'.scrapy\n\n')
        GitIgnore.write(f'# Sphinx documentation\n')
        GitIgnore.write(f'docs/_build/\n\n')
        GitIgnore.write(f'# PyBuilder\n')
        GitIgnore.write(f'.pybuilder/\n')
        GitIgnore.write(f'target/\n\n')
        GitIgnore.write(f'# Jupyter Notebook\n')
        GitIgnore.write(f'.ipynb_checkpoints\n\n')
        GitIgnore.write(f'# IPython\n')
        GitIgnore.write(f'profile_default/\n')
        GitIgnore.write(f'ipython_config.py\n\n')
        GitIgnore.write(f'# pyenv\n')
        GitIgnore.write(f'#   For a library or package, you might want to ignore these files since the code is\n')
        GitIgnore.write(f'#   intended to run in multiple environments; otherwise, check them in:\n')
        GitIgnore.write(f'# .python-version\n\n')
        GitIgnore.write(f'# pipenv\n')
        GitIgnore.write(f'#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.\n')
        GitIgnore.write(f'#   However, in case of collaboration, if having platform-specific dependencies or dependencies\n')
        GitIgnore.write(f"#   having no cross-platform support, pipenv may install dependencies that don't work, or not\n")
        GitIgnore.write(f'#   install all needed dependencies.\n')
        GitIgnore.write(f'#Pipfile.lock\n\n')
        GitIgnore.write(f'# poetry\n')
        GitIgnore.write(f'#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.\n')
        GitIgnore.write(f'#   This is especially recommended for binary packages to ensure reproducibility, and is more\n')
        GitIgnore.write(f'#   commonly ignored for libraries.\n')
        GitIgnore.write(f'#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control\n')
        GitIgnore.write(f'#poetry.lock\n\n')
        GitIgnore.write(f'# pdm\n')
        GitIgnore.write(f'#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.\n')
        GitIgnore.write(f'#pdm.lock\n')
        GitIgnore.write(f'#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it\n')
        GitIgnore.write(f'#   in version control.\n')
        GitIgnore.write(f'#   https://pdm.fming.dev/#use-with-ide\n')
        GitIgnore.write(f'.pdm.toml\n\n')
        GitIgnore.write(f'# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm\n')
        GitIgnore.write(f'__pypackages__/\n\n')
        GitIgnore.write(f'# Celery stuff\n')
        GitIgnore.write(f'celerybeat-schedule\n')
        GitIgnore.write(f'celerybeat.pid\n\n')
        GitIgnore.write(f'# SageMath parsed files\n')
        GitIgnore.write(f'*.sage.py\n\n')
        GitIgnore.write(f'# Environments\n')
        GitIgnore.write(f'.env\n')
        GitIgnore.write(f'.venv\n')
        GitIgnore.write(f'env/\n')
        GitIgnore.write(f'venv/\n')
        GitIgnore.write(f'ENV/\n')
        GitIgnore.write(f'env.bak/\n')
        GitIgnore.write(f'venv.bak/\n\n')
        GitIgnore.write(f'# Spyder project settings\n')
        GitIgnore.write(f'.spyderproject\n')
        GitIgnore.write(f'.spyproject\n\n')
        GitIgnore.write(f'# Rope project settings\n')
        GitIgnore.write(f'.ropeproject\n\n')    
        GitIgnore.write(f'# mkdocs documentation\n')
        GitIgnore.write(f'/site\n\n')
        GitIgnore.write(f'# mypy\n')
        GitIgnore.write(f'.mypy_cache/\n')
        GitIgnore.write(f'.dmypy.json\n')
        GitIgnore.write(f'dmypy.json\n\n')
        GitIgnore.write(f'# Pyre type checker\n')
        GitIgnore.write(f'.pyre/\n\n')
        GitIgnore.write(f'# pytype static type analyzer\n')
        GitIgnore.write(f'.pytype/\n\n')
        GitIgnore.write(f'# Cython debug symbols\n')
        GitIgnore.write(f'cython_debug/\n\n')
        GitIgnore.write(f'# PyCharm\n')
        GitIgnore.write(f'#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can\n')
        GitIgnore.write(f'#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore\n')
        GitIgnore.write(f'#  and can be added to the global gitignore or merged into this file.  For a more nuclear\n')
        GitIgnore.write(f'#  option (not recommended) you can uncomment the following to ignore the entire idea folder.\n')
        GitIgnore.write(f'#.idea/')
        GitIgnore.close()
    print(f'[ O.K ]: Created ".gitignore" File')

def CreateInitFile(AppName, FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as initFile:
        initFile.write(f'## __init__.py File\n')
        initFile.write(f'## Here the contents will be processed to choose the best platform to go\n')
        initFile.write(f'\n')
        initFile.write(f'## Native Libraries\n')
        initFile.write(f'from sys import platform\n')
        initFile.write(f'\n')
        initFile.write(f'## Linux\n')
        initFile.write(f'if platform == "linux" or platform == "linux2":\n')
        initFile.write(f'   from linux import Linux\n')
        initFile.write(f'   Linux.Linux()\n')
        initFile.write(f'\n')
        initFile.write(f'## Mac\n')
        initFile.write(f'elif platform == "darwin":\n')
        initFile.write(f'   from mac import Mac\n')
        initFile.write(f'   Mac.Mac()\n')
        initFile.write(f'\n')
        initFile.write(f'## Windows\n')
        initFile.write(f'elif platform == "win32" or platform == "win64":\n')
        initFile.write(f'   from windows import Windows\n')
        initFile.write(f'   Windows.Windows()\n')
        initFile.close()

def CreateJupyterNotebook(AppName, FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as JupyterFile:
        JupyterFile.write('{\n')
        JupyterFile.write(' "cells": [\n')
        JupyterFile.write('  {\n')
        JupyterFile.write('   "cell_type": "markdown",\n')
        JupyterFile.write('   "metadata": {},\n')
        JupyterFile.write('   "source": [\n')
        JupyterFile.write('    "## External Packages",')
        JupyterFile.write('    "Packages to set before you go",')
        JupyterFile.write('    "<br>Uncomment the code below to install dependencies"')
        JupyterFile.write('   ]\n')
        JupyterFile.write('  },\n')
        JupyterFile.write('  {\n')
        JupyterFile.write('   "cell_type": "code",\n')
        JupyterFile.write('   "execution_count": null,\n')
        JupyterFile.write('   "metadata": {},\n')
        JupyterFile.write('   "outputs": [],\n')
        JupyterFile.write('   "source": [\n')
        JupyterFile.write('    "# %pip install pandas",')
        JupyterFile.write('    "# %pip install numpy",')
        JupyterFile.write('    "# %pip install qgrid",\n')
        JupyterFile.write('    "# %pip install matplotlib",')
        JupyterFile.write('    "# %pip install seaborn"\n')
        JupyterFile.write('   ]\n')
        JupyterFile.write('  },\n')
        JupyterFile.write('  {\n')
        JupyterFile.write('   "cell_type": "markdown",\n')
        JupyterFile.write('   "metadata": {},\n')
        JupyterFile.write('   "source": [\n')
        JupyterFile.write('    "## Check PyBridge Libraries",')
        JupyterFile.write('    "Required libraries will be imported before you run your Jupyter Notebook"\n')
        JupyterFile.write('   ]\n')
        JupyterFile.write('  },\n')
        JupyterFile.write('  {\n')
        JupyterFile.write('   "cell_type": "code",\n')
        JupyterFile.write('   "execution_count": null,\n')
        JupyterFile.write('   "metadata": {},\n')
        JupyterFile.write('   "outputs": [],\n')
        JupyterFile.write('   "source": [\n')
        JupyterFile.write('    "try:",')
        JupyterFile.write('    "   ## Imported Libraries",')
        JupyterFile.write('    "   from sys import platform",')
        JupyterFile.write('    "",')
        JupyterFile.write('    "   ## Local Libraries",')
        JupyterFile.write('    "   from exception import Exceptions",')
        JupyterFile.write('    "except:",')
        JupyterFile.write('    "   raise RuntimeError(\'>> Could not import library: Check if the libraries are installed and run the program again.\')"\n')
        JupyterFile.write('   ]\n')
        JupyterFile.write('  },\n')
        JupyterFile.write('  {\n')
        JupyterFile.write('   "cell_type": "markdown",\n')
        JupyterFile.write('   "metadata": {},\n')
        JupyterFile.write('   "source": [\n')
        JupyterFile.write('    "## Linux Imports",\n')
        JupyterFile.write('    "Imports to use in Linux Environments"\n')
        JupyterFile.write('   ]\n')
        JupyterFile.write('  },\n')
        JupyterFile.write('  {\n')
        JupyterFile.write('   "cell_type": "code",\n')
        JupyterFile.write('   "execution_count": null,\n')
        JupyterFile.write('   "metadata": {},\n')
        JupyterFile.write('   "outputs": [],\n')
        JupyterFile.write('   "source": [\n')
        JupyterFile.write('    "## Linux",\n')
        JupyterFile.write('    "if platform == \\"linux\\" or platform == \\"linux2\\":",\n')
        JupyterFile.write('    "   from linux import FileSystem"\n')
        JupyterFile.write('   ]\n')
        JupyterFile.write('  },\n')
        JupyterFile.write('  {\n')
        JupyterFile.write('   "cell_type": "markdown",\n')
        JupyterFile.write('   "metadata": {},\n')
        JupyterFile.write('   "source": [\n')
        JupyterFile.write('    "## macOS Imports",\n')
        JupyterFile.write('    "Imports to use in macOS Environments"\n')
        JupyterFile.write('   ]\n')
        JupyterFile.write('  },\n')
        JupyterFile.write('  {\n')
        JupyterFile.write('   "cell_type": "code",\n')
        JupyterFile.write('   "execution_count": null,\n')
        JupyterFile.write('   "metadata": {},\n')
        JupyterFile.write('   "outputs": [],\n')
        JupyterFile.write('   "source": [\n')
        JupyterFile.write('    "## Mac",\n')
        JupyterFile.write('    "if platform == \\"darwin\\":",\n')
        JupyterFile.write('    "   from mac import FileSystem"\n')
        JupyterFile.write('   ]\n')
        JupyterFile.write('  },\n')
        JupyterFile.write('  {\n')
        JupyterFile.write('   "cell_type": "markdown",\n')
        JupyterFile.write('   "metadata": {},\n')
        JupyterFile.write('   "source": [\n')
        JupyterFile.write('    "## Windows Imports",')
        JupyterFile.write('    "Imports to use in Windows Environments"\n')
        JupyterFile.write('   ]\n')
        JupyterFile.write('  },\n')
        JupyterFile.write('  {\n')
        JupyterFile.write('   "cell_type": "code",\n')
        JupyterFile.write('   "execution_count": null,\n')
        JupyterFile.write('   "metadata": {},\n')
        JupyterFile.write('   "outputs": [],\n')
        JupyterFile.write('   "source": [\n')
        JupyterFile.write('    "## Windows",\n')
        JupyterFile.write('    "if platform == \\"win32\\" or platform == \\"win64\\":",\n')
        JupyterFile.write('    "   from windows import FileSystem"\n')
        JupyterFile.write('   ]\n')
        JupyterFile.write('  },\n')
        JupyterFile.write('  {\n')
        JupyterFile.write('   "cell_type": "markdown",\n')
        JupyterFile.write('   "metadata": {},\n')
        JupyterFile.write('   "source": [\n')
        JupyterFile.write('    "# Code Implementation",\n')
        JupyterFile.write('    "Here you will implement your code to be executed after imports"\n')
        JupyterFile.write('   ]\n')
        JupyterFile.write('  },\n')
        JupyterFile.write('  {\n')
        JupyterFile.write('   "cell_type": "code",\n')
        JupyterFile.write('   "execution_count": null,\n')
        JupyterFile.write('   "metadata": {},\n')
        JupyterFile.write('   "outputs": [],\n')
        JupyterFile.write('   "source": [\n')
        JupyterFile.write('    "## Examples to make your journey easier",\n')
        JupyterFile.write('    "## Note: Replace the code below with your implementation",\n')
        JupyterFile.write('    "",\n')
        JupyterFile.write('    "# Get the path of your Desktop folder:",\n')
        JupyterFile.write("    \"print(\'{0}{1}'.format('Your Desktop Folder: \', FileSystem.Desktop))\",\n")
        JupyterFile.write('    "\\n",\n')
        JupyterFile.write('    "# Get the path of your Documents folder:",\n')
        JupyterFile.write("    \"print(f\'Your Documents Folder: {FileSystem.Documents}\')\",\n")
        JupyterFile.write('    "\\n",\n')
        JupyterFile.write('    "# Hello World!",\n')
        JupyterFile.write('    "print(\\"Hello World!\\")",\n')
        JupyterFile.write('    "",\n')
        JupyterFile.write('    "# Math Sum",\n')
        JupyterFile.write('    "print(\\">> 2 + 3 =\\", 2 + 3)",\n')
        JupyterFile.write('    "",\n')
        JupyterFile.write('    "# Throw an Exception using native library",\n')
        JupyterFile.write('    "Exceptions.Throw.FileExists()"\n')
        JupyterFile.write('   ]\n')
        JupyterFile.write('  },\n')
        JupyterFile.write('  {\n')
        JupyterFile.write('   "cell_type": "markdown",\n')
        JupyterFile.write('   "metadata": {},\n')
        JupyterFile.write('   "source": [\n')
        JupyterFile.write('    "#",\n')
        JupyterFile.write('    "",\n')
        JupyterFile.write(f'    "Copyright © {datetime.now().year} {getpass.getuser().capitalize()}. All rights reserved."\n')
        JupyterFile.write('   ]\n')
        JupyterFile.write('  }\n')
        JupyterFile.write(' ],\n')
        JupyterFile.write(' "metadata": {\n')
        JupyterFile.write('  "kernelspec": {\n')
        JupyterFile.write('   "display_name": "Python 3.10.4 64-bit",\n')
        JupyterFile.write('   "language": "python",\n')
        JupyterFile.write('   "name": "python3"\n')
        JupyterFile.write('  },\n')
        JupyterFile.write('  "language_info": {\n')
        JupyterFile.write('   "codemirror_mode": {\n')
        JupyterFile.write('    "name": "ipython",\n')
        JupyterFile.write('    "version": 3\n')
        JupyterFile.write('   },\n')
        JupyterFile.write('   "file_extension": ".py",\n')
        JupyterFile.write('   "mimetype": "text/x-python",\n')
        JupyterFile.write('   "name": "python",\n')
        JupyterFile.write('   "nbconvert_exporter": "python",\n')
        JupyterFile.write('   "pygments_lexer": "ipython3",\n')
        JupyterFile.write('   "version": "3.10.5"\n')
        JupyterFile.write('  },\n')
        JupyterFile.write('  "orig_nbformat": 4,\n')
        JupyterFile.write('  "vscode": {\n')
        JupyterFile.write('   "interpreter": {\n')
        JupyterFile.write('    "hash": "aee8b7b246df8f9039afb4144a1f6fd8d2ca17a180786b69acc140d282b71a49"\n')
        JupyterFile.write('   }\n')
        JupyterFile.write('  }\n')
        JupyterFile.write(' },\n')
        JupyterFile.write(' "nbformat": 4,\n')
        JupyterFile.write(' "nbformat_minor": 2\n')
        JupyterFile.write('}\n')
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
        Readme.write(f'{AppName} requires Python {MajorVersion}.{MinorVersion}.{BuildVersion} or later to run\n\n')
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
        Readme.close()
    print(f'[ O.K ]: Created "README" File')

def CreateRequirementsFile(AppName, FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as Requirements:
        Requirements.write(f'"""\n')
        Requirements.write(f'Requirements.py\n\n')
        Requirements.write(f'- This file is used to check if system matches with the minimum requirements to run\n')
        Requirements.write(f'"""\n')
        Requirements.write(f'## Requirements File\n')
        Requirements.write(f'## This file is used to check if system matches with the minimum requirements to run\n\n')
        Requirements.write(f'import sys\n')
        Requirements.write(f'import subprocess\n')
        Requirements.write(f'from exception import Exceptions\n\n')
        Requirements.write(f'## Change "REQUIRE" to "False" to skip system check\n')
        Requirements.write(f'REQUIRE = True\n')
        Requirements.write(f'## Change "REQUIRE" to "True" to allow system check\n\n')
        Requirements.write(f'if REQUIRE == True:\n')
        Requirements.write(f'   ## Target System\n')
        Requirements.write(f'   TargetMajor = 3\n')
        Requirements.write(f'   TargetMinor = 9\n')
        Requirements.write(f'   TargetBuild = 0\n')
        Requirements.write("   TargetVersion = f'{TargetMajor}.{TargetMinor}.{TargetBuild}'\n")
        Requirements.write(f'   ## Target System\n\n')
        Requirements.write(f'   ## Current System\n')
        Requirements.write(f'   MajorVersion = sys.version_info[0]\n')
        Requirements.write(f'   MinorVersion = sys.version_info[1]\n')
        Requirements.write(f'   BuildVersion = sys.version_info[2]\n')
        Requirements.write("   CurrentVersion = f'{MajorVersion}.{MinorVersion}.{BuildVersion}'\n")
        Requirements.write(f'   ## Current System\n\n')
        Requirements.write(f'   ## Uncomment to see information about your system\n')
        Requirements.write("   ## print(f'>> My system current version: Python {CurrentVersion}')\n")
        Requirements.write("   ## print(f'>> Required version to run: Python {TargetVersion}')\n\n")
        Requirements.write(f'   def CheckVersion():\n')
        Requirements.write(f'      if TargetMajor < MajorVersion:\n')
        Requirements.write(f'         Exceptions.Throw.MinorVersion(CurrentVersion, TargetVersion, TargetMinor)\n')
        Requirements.write(f'      elif TargetMajor > MajorVersion:\n')
        Requirements.write(f'         Exceptions.Throw.MajorVersion(CurrentVersion, TargetVersion, MajorVersion)\n')
        Requirements.write(f'      else:\n')
        Requirements.write(f'         if TargetMinor < MinorVersion:\n')
        Requirements.write(f'            Exceptions.Throw.MinorVersion(CurrentVersion, TargetVersion, TargetMinor)\n')
        Requirements.write(f'         elif TargetMinor > MinorVersion:\n')
        Requirements.write(f'            Exceptions.Throw.MajorVersion(CurrentVersion, TargetVersion, MajorVersion)\n')
        Requirements.write(f'         else:\n')
        Requirements.write(f'            if TargetBuild < BuildVersion:\n')
        Requirements.write(f'               Exceptions.Throw.MinorVersion(CurrentVersion, TargetVersion, TargetMinor)\n')
        Requirements.write(f'            elif TargetBuild > BuildVersion:\n')
        Requirements.write(f'               Exceptions.Throw.MajorVersion(CurrentVersion, TargetVersion, MajorVersion)\n')
        Requirements.close()
    print(f'[ O.K ]: Created Requirements Library')

def CreateTwitterFile(AppName, FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as Tokens:
        Tokens.write(f'## Twitter\n')
        Tokens.write(f'## Setup and connect you Twitter account here!\n')
        Tokens.write(f'# Note: DO NOT share your tokens\n')
        Tokens.write(f'## You can generate and regenerate tokens on Twitter Developer Platform\n\n')
        Tokens.write(f'import tweepy\n')
        Tokens.write(f'from tweepy import OAuthHandler\n\n')
        Tokens.write(f'## API Key and API Key Secret\n')
        Tokens.write(f"ConsumerKey = str('')\n")
        Tokens.write(f"ConsumerSecret = str('')\n\n")
        Tokens.write(f'## Access Token and Access Token Secret\n')
        Tokens.write(f'AccessToken = str("")\n')
        Tokens.write(f'AccessTokenSecret = str("")\n\n')
        Tokens.write(f'## Authorization\n')
        Tokens.write(f'Auth = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)\n')
        Tokens.write(f'Auth.set_access_token(AccessToken, AccessTokenSecret)\n\n')
        Tokens.write(f'## Create an API Object\n')
        Tokens.write(f'Twitter = tweepy.API(Auth, wait_on_rate_limit = True)')
        Tokens.close()
    print(f'[ O.K ]: Applied Twitter Application on Environment')

### TARGET OS MODULES
## LinuxApp File
def CreateLinuxAppFile(AppName, FileLocation):
    if ProjectOption == 1:
        with codecs.open(FileLocation, "w", "utf-8-sig") as LinuxAppFile:
            LinuxAppFile.write(f'## LinuxApp File\n')
            LinuxAppFile.write(f'## This file is used to implement code used to run scripts for Linux\n\n')
            LinuxAppFile.write(f'from exception import Exceptions\n')
            LinuxAppFile.write(f'from linux import FileSystem\n\n')
            LinuxAppFile.write(f'def Main():\n')
            LinuxAppFile.write(f'   print("Hello World!")\n\n')
            LinuxAppFile.write(f'Main()\n')
            LinuxAppFile.close()
            
    elif ProjectOption == 2:
        with codecs.open(FileLocation, "w", "utf-8-sig") as LinuxAppFile:
            LinuxAppFile.write(f'## LinuxApp File\n')
            LinuxAppFile.write(f'## This file is used to implement code used to run scripts for Linux\n\n')
            LinuxAppFile.write(f'from exception import Exceptions\n')
            LinuxAppFile.write(f'from linux import FileSystem\n\n')
            LinuxAppFile.write(f'def Main():\n')
            LinuxAppFile.write(f'   while True:\n')
            LinuxAppFile.write(f'      print("="*80)\n')
            LinuxAppFile.write(f'      print(">> Options Menu <<")\n')
            LinuxAppFile.write(f'      print(">> 1. Option One")\n')
            LinuxAppFile.write(f'      print(">> 2. Option Two")\n')
            LinuxAppFile.write(f'      print(">> 3. Option Three")\n\n')
            LinuxAppFile.write(f'      try:\n')
            LinuxAppFile.write(f'         UserInput = int(input(">>[!] Type the option number: "))\n')
            LinuxAppFile.write(f'         print("="*80)\n')
            LinuxAppFile.write(f'         if UserInput == 1:\n')
            LinuxAppFile.write(f'            print("> Option 1")\n')
            LinuxAppFile.write(f'         elif UserInput == 2:\n')
            LinuxAppFile.write(f'            print("> Option 2")\n')
            LinuxAppFile.write(f'         elif UserInput == 3:\n')
            LinuxAppFile.write(f'            print("> Option 3")\n')
            LinuxAppFile.write(f'         else:\n')
            LinuxAppFile.write(f'            print(">> This option is unavailable at this time")\n')
            LinuxAppFile.write(f'      except:\n')
            LinuxAppFile.write(f'         print("-"*80)\n')
            LinuxAppFile.write(f'         print(">> This option is unavailable at this time")\n')
            LinuxAppFile.write(f'         print("-"*80)\n\n')  
            LinuxAppFile.write(f'Main()\n')
            LinuxAppFile.close()

    elif ProjectOption == 3:
        with codecs.open(FileLocation, "w", "utf-8-sig") as LinuxAppFile:
            LinuxAppFile.write(f'## LinuxApp File\n')
            LinuxAppFile.write(f'## This file is used to implement code used to run scripts for Linux\n\n')
            LinuxAppFile.write(f'import Tokens\n')
            LinuxAppFile.write(f'from exception import Exceptions\n')
            LinuxAppFile.write(f'from linux import FileSystem\n\n')
            LinuxAppFile.write(f'def NewTweet():\n')
            LinuxAppFile.write(f'   print("="*80)\n')
            LinuxAppFile.write(f'   print("NEW TWEET")\n')
            LinuxAppFile.write(f'   print("="*80)\n')
            LinuxAppFile.write(f'   Tweet = str(input(">>[!] Whats happening? "))\n')
            LinuxAppFile.write(f'   print("="*80)\n')
            LinuxAppFile.write(f'   print()\n')
            LinuxAppFile.write(f'   print("-"*80)\n')
            LinuxAppFile.write(f'   print(">> Your tweet was sent")\n')
            LinuxAppFile.write(f'   print("-"*80)\n')
            LinuxAppFile.write(f'   print()\n')
            LinuxAppFile.write(f'   print("="*80)\n\n')
            LinuxAppFile.write(f'   try:\n')
            LinuxAppFile.write(f'      Tokens.Twitter.update_status(Tweet)\n')
            LinuxAppFile.write(f"      print(f'>> Your last tweet:')\n")
            LinuxAppFile.write(f"      print(f' > {TweetStr}')\n")
            LinuxAppFile.write(f'      print("-" * 80)\n')
            LinuxAppFile.write(f'   except:\n')
            LinuxAppFile.write(f'      print(">>  Something went wrong: Unabled to connect to Twitter.")\n\n')
            LinuxAppFile.write(f'def Main():\n')
            LinuxAppFile.write(f'   NewTweet()\n\n')
            LinuxAppFile.write(f'Main()\n')
            LinuxAppFile.close()
    print(f'[ O.K ]: Created LinuxApp Library')

## Linux File
def CreateLinuxFile(AppName, FileLocation):
    print("="*80)
    print(">> Creating Linux Module <<")
    print("="*80)
    with codecs.open(FileLocation, "w", "utf-8-sig") as LinuxFile:
        LinuxFile.write(f'## Linux File\n')
        LinuxFile.write(f'## This file is used to implement code used to run scripts for Linux\n')
        LinuxFile.write(f'## Codes implemented here, will run before the script starts running.\n\n')
        LinuxFile.write(f'import os\n')
        LinuxFile.write(f'from linux import FileSystem\n\n')
        LinuxFile.write(f'def Linux():\n')
        LinuxFile.write(f'   ## NOTE: You can use this function\n')
        LinuxFile.write(f'   ## To load information before the app starts running\n\n')
        LinuxFile.write(f'   ## Lets run the SplashScreen\n')
        LinuxFile.write(f'   from linux import SplashScreen\n\n')
        LinuxFile.write(f'   ## Lets check system requirements\n')
        LinuxFile.write(f'   from system import Requirements\n\n')
        LinuxFile.write(f'   ## Start App for Linux\n')
        LinuxFile.write(f'   from linux import LinuxApp\n\n')
        LinuxFile.close()
    print(f'[ O.K ]: Created Linux Library')

## Linux FileSystem
def CreateLinuxFileSystem(AppName, FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as LinuxFS:
        Linux = "User = f'/home/{os.environ"
        FileSystem = '["USER"]}/'
        SUser = f"{Linux}{FileSystem}'"
        LinuxFS.write(f'## FileSystem\n')
        LinuxFS.write(f'## This file contains some default directories of your system\n\n')
        LinuxFS.write(f'import os\n\n')
        LinuxFS.write(f'## Special Directories\n')
        LinuxFS.write(f'CurrentPath = os.getcwd()\n')
        LinuxFS.write(f'{SUser}\n\n')
        LinuxFS.write("Desktop = f'{User}Desktop/'\n")
        LinuxFS.write("Documents = f'{User}Documents/'\n")
        LinuxFS.write("Downloads = f'{User}Downloads/'\n")
        LinuxFS.write("Music = f'{User}Music/'\n\n")
        LinuxFS.write("## Project Directories\n")
        LinuxFS.write("PyBridgeFolder = f'{Documents}PyBridge/'\n")
        LinuxFS.write("ProjectsRepo = f'{PyBridgeFolder}Projects/'\n")
        LinuxFS.write("PythonExtension = '.py'\n")
        LinuxFS.close()
    print(f'[ O.K ]: Created FileSystem Library (Linux)')

## Linux SplashScreen
def CreateLinuxSplashScreen(AppName, FileLocation):
    if ProjectOption == 3:
        with codecs.open(FileLocation, "w", "utf-8-sig") as SplashLinux:
            SplashLinux.write(f'## SplashScreen File\n')
            SplashLinux.write(f'## This file contains information about your project\n\n')
            SplashLinux.write(f'from datetime import date\n\n')
            SplashLinux.write(f'CurrentYear = date.today().year\n')
            SplashLinux.write(f'SoftwareName = "{AppName}"\n')
            SplashLinux.write(f'Version = "1.0"\n')
            SplashLinux.write(f'CopyrightName = "{getpass.getuser().capitalize()}"\n\n')
            SplashLinux.write(f'print("Name:", SoftwareName)\n')
            SplashLinux.write(f'print("Version:", Version)\n')
            SplashLinux.write(f'print("Created By:", CopyrightName)\n\n')
            SplashLinux.write(f'if CurrentYear == 2022:\n')
            SplashLinux.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n')
            SplashLinux.write(f'else:\n')
            SplashLinux.write(f'   print("Copyright © 2022 -", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n\n')
            SplashLinux.write(f'print("="*80)\n')
            SplashLinux.write("print(f'[{SoftwareName} for Linux] - Running...')\n")
            SplashLinux.write(f'print("="*80)\n')
            SplashLinux.write(f"print(f'>> Checking Twitter connection. Please wait...')\n")
            SplashLinux.write(f'print("="*80)\n')
            SplashLinux.write(f'print()')
            SplashLinux.close()
    else:
        with codecs.open(FileLocation, "w", "utf-8-sig") as SplashLinux:
            SplashLinux.write(f'## SplashScreen File\n')
            SplashLinux.write(f'## This file contains information about your project\n\n')
            SplashLinux.write(f'from datetime import date\n\n')
            SplashLinux.write(f'CurrentYear = date.today().year\n')
            SplashLinux.write(f'SoftwareName = "{AppName}"\n')
            SplashLinux.write(f'Version = "1.0"\n')
            SplashLinux.write(f'CopyrightName = "{getpass.getuser().capitalize()}"\n\n')
            SplashLinux.write(f'print("Name:", SoftwareName)\n')
            SplashLinux.write(f'print("Version:", Version)\n')
            SplashLinux.write(f'print("Created By:", CopyrightName)\n\n')
            SplashLinux.write(f'if CurrentYear == 2022:\n')
            SplashLinux.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n')
            SplashLinux.write(f'else:\n')
            SplashLinux.write(f'   print("Copyright © 2022 -", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n\n')
            SplashLinux.write(f'print("="*80)\n')
            SplashLinux.write("print(f'[{SoftwareName} for Linux] - Running...')\n")
            SplashLinux.write(f'print("="*80)\n')
            SplashLinux.write(f'print()\n')
            SplashLinux.close()
    print(f'[ O.K ]: Created SplashScreen Library')

## MacApp File
def CreateMacAppFile(AppName, FileLocation):
    if ProjectOption == 1:
        with codecs.open(FileLocation, "w", "utf-8-sig") as MacAppFile:
            MacAppFile.write(f'## MacApp File\n')
            MacAppFile.write(f'## This file is used to implement code used to run scripts for Mac\n\n')
            MacAppFile.write(f'from exception import Exceptions\n')
            MacAppFile.write(f'from mac import FileSystem\n\n')
            MacAppFile.write(f'def Main():\n')
            MacAppFile.write(f'   print("Hello World!")\n\n')
            MacAppFile.write(f'Main()\n')
            MacAppFile.close()

    elif ProjectOption == 2:
        with codecs.open(FileLocation, "w", "utf-8-sig") as MacAppFile:
            MacAppFile.write(f'## MacApp File\n')
            MacAppFile.write(f'## This file is used to implement code used to run scripts for Mac\n\n')
            MacAppFile.write(f'from exception import Exceptions\n')
            MacAppFile.write(f'from mac import FileSystem\n\n')
            MacAppFile.write(f'def Main():\n')
            MacAppFile.write(f'   while True:\n')
            MacAppFile.write(f'      print("="*80)\n')
            MacAppFile.write(f'      print(">> Options Menu <<")\n')
            MacAppFile.write(f'      print(">> 1. Option One")\n')
            MacAppFile.write(f'      print(">> 2. Option Two")\n')
            MacAppFile.write(f'      print(">> 3. Option Three")\n\n')
            MacAppFile.write(f'      try:\n')
            MacAppFile.write(f'         UserInput = int(input(">>[!] Type the option number: "))\n')
            MacAppFile.write(f'         print("="*80)\n')
            MacAppFile.write(f'         if UserInput == 1:\n')
            MacAppFile.write(f'            print("> Option 1")\n')
            MacAppFile.write(f'         elif UserInput == 2:\n')
            MacAppFile.write(f'            print("> Option 2")\n')
            MacAppFile.write(f'         elif UserInput == 3:\n')
            MacAppFile.write(f'            print("> Option 3")\n')
            MacAppFile.write(f'         else:\n')
            MacAppFile.write(f'            print(">> This option is unavailable at this time")\n')
            MacAppFile.write(f'      except:\n')
            MacAppFile.write(f'         print("-"*80)\n')
            MacAppFile.write(f'         print(">> This option is unavailable at this time")\n')
            MacAppFile.write(f'         print("-"*80)\n\n')
            MacAppFile.write(f'Main()\n')
            MacAppFile.close()

    elif ProjectOption == 3:
        with codecs.open(FileLocation, "w", "utf-8-sig") as MacAppFile:
            MacAppFile.write(f'## MacApp File\n')
            MacAppFile.write(f'## This file is used to implement code used to run scripts for Mac\n\n')
            MacAppFile.write(f'import Tokens\n')
            MacAppFile.write(f'from exception import Exceptions\n')
            MacAppFile.write(f'from mac import FileSystem\n\n')
            MacAppFile.write(f'def NewTweet():\n')
            MacAppFile.write(f'   print("="*80)\n')
            MacAppFile.write(f'   print("NEW TWEET")\n')
            MacAppFile.write(f'   print("="*80)\n')
            MacAppFile.write(f'   Tweet = str(input(">>[!] Whats happening? "))\n')
            MacAppFile.write(f'   print("="*80)\n')
            MacAppFile.write(f'   print()\n')
            MacAppFile.write(f'   print("-"*80)\n')
            MacAppFile.write(f'   print(">> Your tweet was sent")\n')
            MacAppFile.write(f'   print("-"*80)\n')
            MacAppFile.write(f'   print()\n')
            MacAppFile.write(f'   print("="*80)\n\n')
            MacAppFile.write(f'   try:\n')
            MacAppFile.write(f'      Tokens.Twitter.update_status(Tweet)\n')
            MacAppFile.write(f"      print(f'>> Your last tweet:')\n")
            MacAppFile.write(f"      print(f' > {TweetStr}')\n")
            MacAppFile.write(f'      print("-" * 80)\n')
            MacAppFile.write(f'   except:\n')
            MacAppFile.write(f'      print(">>  Something went wrong: Unabled to connect to Twitter.")\n\n') 
            MacAppFile.write(f'def Main():\n')
            MacAppFile.write(f'   NewTweet()\n\n')
            MacAppFile.write(f'Main()\n')
            MacAppFile.close()
    print(f'[ O.K ]: Created MacApp Library')

## Mac File
def CreateMacFile(AppName, FileLocation):
    print("="*80)
    print(">> Creating Mac Module <<")
    print("="*80)
    with codecs.open(FileLocation, "w", "utf-8-sig") as MacFile:
        MacFile.write(f'## Mac File\n')
        MacFile.write(f'## This file is used to implement code used to run scripts for Mac\n')
        MacFile.write(f'## Codes implemented here, will run before the script starts running.\n\n')
        MacFile.write(f'import os\n')
        MacFile.write(f'from mac import FileSystem\n\n')
        MacFile.write(f'def Mac():\n')
        MacFile.write(f'   ## NOTE: You can use this function\n')
        MacFile.write(f'   ## To load information before the app starts running\n\n')
        MacFile.write(f'   ## Lets run the SplashScreen\n')
        MacFile.write(f'   from mac import SplashScreen\n\n')
        MacFile.write(f'   ## Lets check system requirements\n')
        MacFile.write(f'   from system import Requirements\n\n')
        MacFile.write(f'   ## Start App for Mac\n')
        MacFile.write(f'   from mac import MacApp\n\n')
        MacFile.close()
    print("[ O.K ]: Created Mac Library")

## Mac FileSystem
def CreateMacFileSystem(AppName, FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as MacFS:
        Mac = "User = f'/Users/{os.environ"
        FileSystem = '["USER"]}/'
        SUser = f"{Mac}{FileSystem}'"
        MacFS.write(f'## FileSystem\n')
        MacFS.write(f'## This file contains some default directories of your system\n\n')
        MacFS.write(f'import os\n\n')
        MacFS.write(f'## Special Directories\n')
        MacFS.write(f'CurrentPath = os.getcwd()\n')
        MacFS.write(f'{SUser}\n')
        MacFS.write("Applications = f'{User}Applications/'\n")
        MacFS.write("Desktop = f'{User}Desktop/'\n")
        MacFS.write("Documents = f'{User}Documents/'\n")
        MacFS.write("Downloads = f'{User}Downloads/'\n")
        MacFS.write("Movies = f'{User}Movies/'\n")
        MacFS.write("Music = f'{User}Music/'\n")
        MacFS.write("Pictures = f'{User}Pictures/'\n")
        MacFS.write("Public = f'{User}Public/'\n\n")
        MacFS.write("## Project Directories\n")
        MacFS.write("PyBridgeFolder = f'{Documents}PyBridge/'\n")
        MacFS.write("ProjectsRepo = f'{PyBridgeFolder}Projects/'\n")
        MacFS.write("PythonExtension = '.py'\n")
        MacFS.close()
    print("[ O.K ]: Created FileSystem Library (macOS)")

## Mac SplashScreen
def CreateMacSplashScreen(AppName, FileLocation):
    if ProjectOption == 3:
        with codecs.open(FileLocation, "w", "utf-8-sig") as SplashMac:
            SplashMac.write(f'## SplashScreen File\n')
            SplashMac.write(f'## This file contains information about your project\n\n')
            SplashMac.write(f'from datetime import date\n\n')
            SplashMac.write(f'CurrentYear = date.today().year\n')
            SplashMac.write(f'SoftwareName = "{AppName}"\n')
            SplashMac.write(f'Version = "1.0"\n')
            SplashMac.write(f'CopyrightName = "{getpass.getuser().capitalize()}"\n\n')
            SplashMac.write(f'print("Name:", SoftwareName)\n')
            SplashMac.write(f'print("Version:", Version)\n')
            SplashMac.write(f'print("Created By:", CopyrightName)\n\n')
            SplashMac.write(f'if CurrentYear == 2022:\n')
            SplashMac.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n')
            SplashMac.write(f'else:\n')
            SplashMac.write(f'   print("Copyright © 2022 -", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n\n')
            SplashMac.write(f'print("="*80)\n')
            SplashMac.write("print(f'[{SoftwareName} for Mac] - Running...')\n")
            SplashMac.write(f'print("="*80)\n')
            SplashMac.write(f"print(f'>> Checking Twitter connection. Please wait...')\n")
            SplashMac.write(f'print("="*80)\n')
            SplashMac.write(f'print()')
            SplashMac.close()
    else:
        with codecs.open(FileLocation, "w", "utf-8-sig") as SplashMac:
            SplashMac.write(f'## SplashScreen File\n')
            SplashMac.write(f'## This file contains information about your project\n\n')
            SplashMac.write(f'from datetime import date\n\n')
            SplashMac.write(f'CurrentYear = date.today().year\n')
            SplashMac.write(f'SoftwareName = "{AppName}"\n')
            SplashMac.write(f'Version = "1.0"\n')
            SplashMac.write(f'CopyrightName = "{getpass.getuser().capitalize()}"\n\n')
            SplashMac.write(f'print("Name:", SoftwareName)\n')
            SplashMac.write(f'print("Version:", Version)\n')
            SplashMac.write(f'print("Created By:", CopyrightName)\n\n')
            SplashMac.write(f'if CurrentYear == 2022:\n')
            SplashMac.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n')
            SplashMac.write(f'else:\n')
            SplashMac.write(f'   print("Copyright © 2022 -", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n\n')
            SplashMac.write(f'print("="*80)\n')
            SplashMac.write("print(f'[{SoftwareName} for Mac] - Running...')\n")
            SplashMac.write(f'print("="*80)\n')
            SplashMac.write(f'print()\n')
            SplashMac.close()
    print("[ O.K ]: Created SplashScreen Library")

## WindowsApp File
def CreateWindowsAppFile(AppName, FileLocation):
    if ProjectOption == 1:
        with codecs.open(FileLocation, "w", "utf-8-sig") as WindowsAppFile:
            WindowsAppFile.write(f'## WindowsApp File\n')
            WindowsAppFile.write(f'## This file is used to implement code used to run scripts for Windows\n\n')
            WindowsAppFile.write(f'from exception import Exceptions\n')
            WindowsAppFile.write(f'from windows import FileSystem\n\n')
            WindowsAppFile.write(f'def Main():\n')
            WindowsAppFile.write(f'   print("Hello World!")\n\n') 
            WindowsAppFile.write(f'Main()\n')
            WindowsAppFile.close()
            
    elif ProjectOption == 2:
        with codecs.open(FileLocation, "w", "utf-8-sig") as WindowsAppFile:
            WindowsAppFile.write(f'## WindowsApp File\n')
            WindowsAppFile.write(f'## This file is used to implement code used to run scripts for Windows\n\n')
            WindowsAppFile.write(f'from exception import Exceptions\n')
            WindowsAppFile.write(f'from windows import FileSystem\n\n')
            WindowsAppFile.write(f'def Main():\n')
            WindowsAppFile.write(f'   while True:\n')
            WindowsAppFile.write(f'      print("="*80)\n')
            WindowsAppFile.write(f'      print(">> Options Menu <<")\n')
            WindowsAppFile.write(f'      print(">> 1. Option One")\n')
            WindowsAppFile.write(f'      print(">> 2. Option Two")\n')
            WindowsAppFile.write(f'      print(">> 3. Option Three")\n\n')
            WindowsAppFile.write(f'      try:\n')
            WindowsAppFile.write(f'         UserInput = int(input(">>[!] Type the option number: "))\n')
            WindowsAppFile.write(f'         print("="*80)\n')
            WindowsAppFile.write(f'         if UserInput == 1:\n')
            WindowsAppFile.write(f'            print("> Option 1")\n')
            WindowsAppFile.write(f'         elif UserInput == 2:\n')
            WindowsAppFile.write(f'            print("> Option 2")\n')
            WindowsAppFile.write(f'         elif UserInput == 3:\n')
            WindowsAppFile.write(f'            print("> Option 3")\n')
            WindowsAppFile.write(f'         else:\n')
            WindowsAppFile.write(f'            print(">> This option is unavailable at this time")\n')
            WindowsAppFile.write(f'      except:\n')
            WindowsAppFile.write(f'         print("-"*80)\n')
            WindowsAppFile.write(f'         print(">> This option is unavailable at this time")\n')
            WindowsAppFile.write(f'         print("-"*80)\n\n')  
            WindowsAppFile.write(f'Main()\n')
            WindowsAppFile.close()
        
    elif ProjectOption == 3:
        with codecs.open(FileLocation, "w", "utf-8-sig") as WindowsAppFile:
            WindowsAppFile.write(f'## WindowsApp File\n')
            WindowsAppFile.write(f'## This file is used to implement code used to run scripts for Windows\n\n')
            WindowsAppFile.write(f'import Tokens\n')
            WindowsAppFile.write(f'from exception import Exceptions\n')
            WindowsAppFile.write(f'from windows import FileSystem\n\n')
            WindowsAppFile.write(f'def NewTweet():\n')
            WindowsAppFile.write(f'   print("="*80)\n')
            WindowsAppFile.write(f'   print("NEW TWEET")\n')
            WindowsAppFile.write(f'   print("="*80)\n')
            WindowsAppFile.write(f'   Tweet = str(input(">>[!] Whats happening? "))\n')
            WindowsAppFile.write(f'   print("="*80)\n')
            WindowsAppFile.write(f'   print()\n')
            WindowsAppFile.write(f'   print("-"*80)\n')
            WindowsAppFile.write(f'   print(">> Your tweet was sent")\n')
            WindowsAppFile.write(f'   print("-"*80)\n')
            WindowsAppFile.write(f'   print()\n')
            WindowsAppFile.write(f'   print("="*80)\n\n')
            WindowsAppFile.write(f'   try:\n')
            WindowsAppFile.write(f'      Tokens.Twitter.update_status(Tweet)\n')
            WindowsAppFile.write(f"      print(f'>> Your last tweet:')\n")
            WindowsAppFile.write(f"      print(f' > {TweetStr}')\n")
            WindowsAppFile.write(f'      print("-" * 80)\n')
            WindowsAppFile.write(f'   except:\n')
            WindowsAppFile.write(f'      print(">>  Something went wrong: Unabled to connect to Twitter.")\n\n')  
            WindowsAppFile.write(f'def Main():\n')
            WindowsAppFile.write(f'   NewTweet()\n\n')
            WindowsAppFile.write(f'Main()\n')
            WindowsAppFile.close()
    print(f'[ O.K ]: Created WindowsApp Library')

## Windows File
def CreateWindowsFile(AppName, FileLocation):
    print("="*80)
    print(">> Creating Windows Module <<")
    print("="*80)

    with codecs.open(FileLocation, "w", "utf-8-sig") as WindowsFile:
        WindowsFile.write(f'## Windows File\n')
        WindowsFile.write(f'## This file is used to implement code used to run scripts for Windows\n')
        WindowsFile.write(f'## Codes implemented here, will run before the script starts running.\n\n')
        WindowsFile.write(f'import os\n')
        WindowsFile.write(f'from windows import FileSystem\n\n')
        WindowsFile.write(f'def Windows():\n')
        WindowsFile.write(f'   ## NOTE: You can use this function\n')
        WindowsFile.write(f'   ## To load information before the app starts running\n\n')
        WindowsFile.write(f'   ## Lets run the SplashScreen\n')
        WindowsFile.write(f'   from windows import SplashScreen\n\n')
        WindowsFile.write(f'   ## Lets check system requirements\n')
        WindowsFile.write(f'   from system import Requirements\n\n')
        WindowsFile.write(f'   ## Start App for Windows\n')
        WindowsFile.write(f'   from windows import WindowsApp\n\n')
        WindowsFile.close()
    print("[ O.K ]: Created Windows Library")

## Windows FileSystem
def CreateWindowsFileSystem(AppName, FileLocation):
    with codecs.open(FileLocation, "w", "utf-8-sig") as WindowsFS:
        WindowsFS.write(f'## FileSystem\n')
        WindowsFS.write(f'## This file contains some default directories of your system\n\n')
        WindowsFS.write(f'import os\n\n')
        WindowsFS.write(f'## Special Directories\n')
        WindowsFS.write(f'CurrentPath = os.getcwd()\n')
        WindowsFS.write(f"User = os.environ['USERPROFILE']\n")
        WindowsFS.write("ApplicationData = f'{User}/AppData/Roaming/'\n")
        WindowsFS.write("Desktop = f'{User}/Desktop/'\n")
        WindowsFS.write("Documents = f'{User}/Documents/'\n")
        WindowsFS.write("Downloads = f'{User}/Downloads/'\n")
        WindowsFS.write("LocalAppData = f'{User}/AppData/Local/'\n")
        WindowsFS.write("Temp = f'{LocalAppData}Temp'\n")
        WindowsFS.write("Pictures = f'{User}/Pictures/'\n")
        WindowsFS.write("Favorites = f'{User}/Favorites/'\n\n")
        WindowsFS.write("## Project Directories\n")
        WindowsFS.write("PyBridgeFolder = f'{Documents}PyBridge/'\n")
        WindowsFS.write("ProjectsRepo = f'{PyBridgeFolder}Projects/'\n")
        WindowsFS.write("PythonExtension = '.py'\n")
        WindowsFS.close()
    print("[ O.K ]: Created FileSystem Library (Windows)")

## Windows SplashScreen
def CreateWindowsSplashScreen(AppName, FileLocation):
    if ProjectOption == 3:
        with codecs.open(FileLocation, "w", "utf-8-sig") as SplashWindows:
            SplashWindows.write(f'## SplashScreen File\n')
            SplashWindows.write(f'## This file contains information about your project\n\n')
            SplashWindows.write(f'from datetime import date\n\n')
            SplashWindows.write(f'CurrentYear = date.today().year\n')
            SplashWindows.write(f'SoftwareName = "{AppName}"\n')
            SplashWindows.write(f'Version = "1.0"\n')
            SplashWindows.write(f'CopyrightName = "{getpass.getuser().capitalize()}"\n\n')
            SplashWindows.write(f'print("Name:", SoftwareName)\n')
            SplashWindows.write(f'print("Version:", Version)\n')
            SplashWindows.write(f'print("Created By:", CopyrightName)\n\n')
            SplashWindows.write(f'if CurrentYear == 2022:\n')
            SplashWindows.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n')
            SplashWindows.write(f'else:\n')
            SplashWindows.write(f'   print("Copyright © 2022 -", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n\n')
            SplashWindows.write(f'print("="*80)\n')
            SplashWindows.write("print(f'[{SoftwareName} for Windows] - Running...')\n")
            SplashWindows.write(f'print("="*80)\n')
            SplashWindows.write(f"print(f'>> Checking Twitter connection. Please wait...')\n")
            SplashWindows.write(f'print("="*80)\n')
            SplashWindows.write(f'print()')
            SplashWindows.close()
    else:
        with codecs.open(FileLocation, "w", "utf-8-sig") as SplashWindows:
            SplashWindows.write(f'## SplashScreen File\n')
            SplashWindows.write(f'## This file contains information about your project\n\n')
            SplashWindows.write(f'from datetime import date\n\n')
            SplashWindows.write(f'CurrentYear = date.today().year\n')
            SplashWindows.write(f'SoftwareName = "{AppName}"\n')
            SplashWindows.write(f'Version = "1.0"\n')
            SplashWindows.write(f'CopyrightName = "{getpass.getuser().capitalize()}"\n\n')
            SplashWindows.write(f'print("Name:", SoftwareName)\n')
            SplashWindows.write(f'print("Version:", Version)\n')
            SplashWindows.write(f'print("Created By:", CopyrightName)\n\n')
            SplashWindows.write(f'if CurrentYear == 2022:\n')
            SplashWindows.write(f'   print("Copyright ©", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n')
            SplashWindows.write(f'else:\n')
            SplashWindows.write(f'   print("Copyright © 2022 -", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")\n\n')
            SplashWindows.write(f'print("="*80)\n')
            SplashWindows.write("print(f'[{SoftwareName} for Windows] - Running...')\n")
            SplashWindows.write(f'print("="*80)\n')
            SplashWindows.write(f'print()\n')
            SplashWindows.close()
    print("[ O.K ]: Created SplashScreen Library")
### TARGET OS MODULES

def CreateBridge():
    print("="*80)
    print(">> CREATE PROJECT <<")
    print("="*80)
    print(f'>> {ProjectType} <<')
    print("="*80)
    UserInput = str(input(">>[!] Project Name: "))
    print(f'>> Creating bridge to the project "{UserInput}"...')
    print("="*80)
    print()
    
    try:
        AppLocation = f'{FileSystem.ProjectsRepo}{UserInput}/'
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
    systemPath = f'{AppLocation}system/'
    exceptionPath = f'{AppLocation}exception/'
    linuxPath = f'{AppLocation}linux/'
    macPath = f'{AppLocation}mac/'
    windowsPath = f'{AppLocation}windows/'

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
    gitignoreFile = f'{AppLocation}.gitignore'
    initFile = f'{AppLocation}__init__.py'
    jupyterFile = f'{AppLocation}{AppName}.ipynb'
    readmeFile = f'{AppLocation}README.md'
    twitterFile = f'{AppLocation}Twitter.py'
    ## Root Files

    ## System and Exceptions Files
    exceptionsFile = f'{exceptionPath}Exceptions.py'
    requirementsFile = f'{systemPath}Requirements.py'
    ## System and Exceptions Files

    ## Linux Files
    linuxFSFile = f'{linuxPath}FileSystem.py'
    linuxFile = f'{linuxPath}Linux.py'
    linuxAppFile = f'{linuxPath}LinuxApp.py'
    splashLinuxFile = f'{linuxPath}SplashScreen.py'
    ## Linux Files

    ## Mac Files
    macFSFile = f'{macPath}FileSystem.py'
    macFile = f'{macPath}Mac.py'
    macAppFile = f'{macPath}MacApp.py'
    splashMacFile = f'{macPath}SplashScreen.py'
    ## Mac Files

    ## Windows Files
    windowsFSFile = f'{windowsPath}FileSystem.py'
    windowsFile = f'{windowsPath}Windows.py'
    windowsAppFile = f'{windowsPath}WindowsApp.py'
    splashWindowsFile = f'{windowsPath}SplashScreen.py'
    ## Windows Files
    ### GENERATE LIBRARIES FOR THE BRIDGE

    ### CRETE BRIDGE
    print("=" * 80)
    print(f'>> Creating {AppName} Libraries and Files <<')
    print("=" * 80)
    CreateExceptionsFile(AppName, exceptionsFile)
    CreateGitIgnoreFile(AppName, gitignoreFile)
    CreateReadmeFile(AppName, readmeFile)
    CreateRequirementsFile(AppName, requirementsFile)

    startTime = time.time()
    if ProjectOption == 1:
        print()
        CreateInitFile(AppName, initFile) ## Hbisneto
        
        CreateLinuxFile(AppName, linuxFile)
        CreateLinuxAppFile(AppName, linuxAppFile)
        CreateLinuxFileSystem(AppName, linuxFSFile)
        CreateLinuxSplashScreen(AppName, splashLinuxFile)
        
        CreateMacFile(AppName, macFile)
        CreateMacAppFile(AppName, macAppFile)
        CreateMacFileSystem(AppName, macFSFile)
        CreateMacSplashScreen(AppName, splashMacFile)
        
        CreateWindowsFile(AppName, windowsFile)
        CreateWindowsAppFile(AppName, windowsAppFile)
        CreateWindowsFileSystem(AppName, windowsFSFile)
        CreateWindowsSplashScreen(AppName, splashWindowsFile)
    elif ProjectOption == 2:
        print()
        CreateInitFile(AppName, initFile)
        
        CreateLinuxFile(AppName, linuxFile)
        CreateLinuxAppFile(AppName, linuxAppFile)
        CreateLinuxFileSystem(AppName, linuxFSFile)
        CreateLinuxSplashScreen(AppName, splashLinuxFile)
        
        CreateMacFile(AppName, macFile)
        CreateMacAppFile(AppName, macAppFile)
        CreateMacFileSystem(AppName, macFSFile)
        CreateMacSplashScreen(AppName, splashMacFile)
        
        CreateWindowsFile(AppName, windowsFile)
        CreateWindowsAppFile(AppName, windowsAppFile)
        CreateWindowsFileSystem(AppName, windowsFSFile)
        CreateWindowsSplashScreen(AppName, splashWindowsFile)
    elif ProjectOption == 3:
        CreateInitFile(AppName, initFile)
        CreateTwitterFile(AppName, twitterFile)
        
        CreateLinuxFile(AppName, linuxFile)
        CreateLinuxAppFile(AppName, linuxAppFile)
        CreateLinuxFileSystem(AppName, linuxFSFile)
        CreateLinuxSplashScreen(AppName, splashLinuxFile)
        
        CreateMacFile(AppName, macFile)
        CreateMacAppFile(AppName, macAppFile)
        CreateMacFileSystem(AppName, macFSFile)
        CreateMacSplashScreen(AppName, splashMacFile)
        
        CreateWindowsFile(AppName, windowsFile)
        CreateWindowsAppFile(AppName, windowsAppFile)
        CreateWindowsFileSystem(AppName, windowsFSFile)
        CreateWindowsSplashScreen(AppName, splashWindowsFile)
    elif ProjectOption == 4:
        CreateJupyterNotebook(AppName, jupyterFile)

        CreateLinuxFileSystem(AppName, linuxFSFile)
        CreateMacFileSystem(AppName, macFSFile)
        CreateWindowsFileSystem(AppName, windowsFSFile)
    print()

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
    cmd = subprocess.getoutput(f'open {AppLocation}')

    userInput = str(input(">> Would you like to open project in Visual Studio Code? [Y/n]: "))

    if userInput == "Y" or userInput == "y":
        cmd = subprocess.getoutput(f'cd {AppLocation}')
        cmd = subprocess.getoutput(f'code .')

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