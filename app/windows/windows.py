"""
### windows.py

- This file is used to implement code used to run scripts for Windows
- Codes implemented here, will run before the main script starts running
"""
## Windows File
## This file is used to implement code used to run scripts for Windows
## Codes implemented here, will run before the main script starts running

import info
import filesystem as fs
from filesystem import wrapper as wr
from system import core
from system import requirements as req
import pybridge

def windows():
   ## NOTE: You can use this function
   ## To load information before the app starts running

   ## Lets get Application Info (info.py)
   info.loadSplashScreen()

   ## Lets check system requirements
   req.check_version()

   ### You just need to run ONCE: Be sure you commented this code after first run
   # req.install_dependencies()
   ### You just need to run ONCE: Be sure you commented this code after first run

   ### Creates all needed folders
   wr.create_directory(f'{fs.documents}/{info.NAME}/Repository')

   ## Start App for Windows
   pybridge.start()