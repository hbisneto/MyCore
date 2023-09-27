"""
### Mac.py

- This file is used to implement code used to run scripts for Mac
- Codes implemented here, will run before the main script starts running
"""
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