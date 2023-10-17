"""
### linux.py

- This file is used to implement code used to run scripts for Mac
- Codes implemented here, will run before the main script starts running
"""
## Mac File
## This file is used to implement code used to run scripts for Mac
## Codes implemented here, will run before the main script starts running

import app
import info
from system import filesystem as fs
from system import requirements as req

def linux():
   ## NOTE: You can use this function
   ## To load information before the app starts running

   ## Lets get Application Info (APPINFO.py)
   info.loadSplashScreen()

   ## Lets check system requirements
   req.check_version()

   ### You just need to run ONCE: Be sure you commented this code after first run
   # Requirements.InstallDependencies()
   ### You just need to run ONCE: Be sure you commented this code after first run

   ### Creates all needed folders
   fs.create_custom_folder(info.NAME, fs.documents)
   fs.create_custom_folder("Repository", f'{fs.documents}/{info.NAME}')

   ## Start App for Mac
   app.start()