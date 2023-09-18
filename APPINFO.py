"""
### APPINFO.py

- This file contains information about your project
"""

import getpass
from datetime import date
from datetime import datetime
from sys import platform

NAME = "MyCore"
VERSION = "1.7"
COPYRIGHT = "Heitor Bisneto"
TYPE = "Menu Application Loop"
LICENCE = "MIT"
LOCALUSERNAME = getpass.getuser().capitalize()

CurrentYear = date.today().year
Now = datetime.now()
Hour = int(Now.strftime("%H"))
TimeAccess = Now.strftime("%H:%M:%S")
platformName = ""

### UNCOMMENT TO USE VARIABLES
# Minute = int(Now.strftime("%M"))
# Second = int(Now.strftime("%S"))
### UNCOMMENT TO USE VARIABLES
        
def loadSplashScreen():
    print("="*80)
    print(f'[{NAME} for {platformName}] - Running...')
    print("="*80)

    print(f'Name: {NAME}')
    print(f'Version: {VERSION}')
    print(f'Created By: {COPYRIGHT}')

    if CurrentYear == 2021:
        print(f'Copyright © {CurrentYear} | {COPYRIGHT}. All rights reserved.')
        print("="*80)
    else:
        print(f'Copyright © 2021 - {CurrentYear} | {COPYRIGHT}. All rights reserved.')
        print("="*80)

    if Hour >= 6 and Hour < 12:
        DayPeriod = "Morning"
        print(f'Hello {LOCALUSERNAME}. Good {DayPeriod}! - {TimeAccess}')
        print("="*80)
    elif Hour >= 12 and Hour < 18:
        DayPeriod = "Afternoon"
        print(f'Hello {LOCALUSERNAME}. Good {DayPeriod}! - {TimeAccess}')
        print("="*80)
    elif Hour >= 18 and Hour != 0:
        DayPeriod = "Evening"
        print(f'Hello {LOCALUSERNAME}. Good {DayPeriod}! - {TimeAccess}')
        print("="*80)
    else:
        print(f'Hello {LOCALUSERNAME}. Nice to see you! - {TimeAccess}')
        print("="*80)

## Linux
if platform == "linux" or platform == "linux2":
    platformName = "Linux"
## Mac
elif platform == "darwin":
    platformName = "Mac"
## Windows
elif platform == "win32" or platform == "win64":
    platformName = "Windows"