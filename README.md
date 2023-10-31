---
This project was created using [PyBridge](https://github.com/hbisneto/PyBridge)

---

# MyCore

### Novidades dessa versão
---

```
.
├── __init__.py
├── exception
│ ├── Exceptions.py
├── system
│ ├── SystemRequirements.py
├── linux
│ ├── Linux.py
│ ├── LinuxApp.py
│ ├── FileSystem.py
│ └── SplashScreen.py
├── mac
│ ├── Mac.py
│ ├── MacApp.py
│ ├── FileSystem.py
│ └── SplashScreen.py
├── windows
│ ├── Windows.py
│ ├── WindowsApp.py
│ ├── FileSystem.py
│ └── SplashScreen.py
├── twitter.py
└── README.md
```

**Environment**

- Improvements in CLI (Command Line Interface)
- Improved System Logs (in Logs.py)
- Improved Jupyter Notebooks file

**Core**

A biblioteca **Core.py** foi realocada para o módulo system.
<br>
Isso permitiu que o código fosse implementado apenas uma vez, tornando o processo mais eficiente.

- Fixed a bug when user input text instead of a number in MenuOption

**Requirements**

- Improved System Requirements (in Requirements.py):
- Added new InstallDependencies function.
- Removed CheckMajorVersion and CheckMinorVersion functions from library (added CheckVersion function instead)
 
**FileSystem**

A biblioteca **FileSystem.py**, presente em todos os módulos de sistema, foi reestruturada.
<br>
Nessa versão, a biblioteca FileSystem.py foi elevada, possibilitando o suporte para mais de um sistema operacional sem a necessidade de multiplas implementações. Independente da plataforma.

- Padronização dos diretórios no sistema
- A pasta do usuário "Music" do Windows foi adicionado ao FileSystem.py 
- As URLs do sistema de arquivos foram padronizadas: Terminando sem a barra (/)

A estrutura da biblioteca foi organizada da seguinte maneira:

```
## FileSystem
## This file contains some default directories of your system
## You can use this file to implement custom directories used by your application

### NATIVE LIBRARIES ###
import os
from sys import platform
from system import APPINFO
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

```

Dessa forma, diretórios padrões como Desktop e Documents serão carregados quando o programa estiver em execução independente do sistema operacional usado.
<br>
Também foram incluidos diretórios únicos de cada sistema operacional como o diretório Templates no Linux, Applications no macOS, e Favorites no Windows.

Algumas bibliotecas foram realocadas no sistema:

```

```


## Requirements

MyCore requires Python 3.9.0 or later to run

## Installation

```
pip install MyCore
```

## External Links

Here is some external links that you can use in your `README.md` file.

- [First Link](https://google.com)
- [Second Link](https://google.com)
- [Third Link](https://google.com)

#

Copyright © 2023 Heitor. All rights reserved.





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