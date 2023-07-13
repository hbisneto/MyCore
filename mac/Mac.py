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
from system import SplashScreen
# from mac import MacApp

def Mac():
   ## NOTE: You can use this function
   ## To load information before the app starts running

   ## Lets run the SplashScreen
   SplashScreen.Show()

   ## Lets check system requirements
   Requirements.CheckVersion()

   ### You just need to run ONCE: Be sure you commented this code after first run
   ### Requirements.InstallDependencies()
   ### You just need to run ONCE: Be sure you commented this code after first run

   ### Verify environment folders
   FileSystem.CreateEnvironmentFolders()

   ## Start App for Mac
   # MacApp.Run()
   App.Run()