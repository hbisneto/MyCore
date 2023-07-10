"""
### SplashScreen.py

- This file contains information about your project
"""
## SplashScreen File
## This file contains information about your project

import getpass
import APPINFO
from datetime import date
from datetime import datetime

CurrentYear = date.today().year

Now = datetime.now()
Hour = int(Now.strftime("%H"))
Minute = int(Now.strftime("%M"))
Second = int(Now.strftime("%S"))
TimeAccess = Now.strftime("%H:%M:%S")

def Show():    
    print("="*80)
    print(f'[{APPINFO.NAME}] - Running...')
    print("="*80)

    print(f'Name: {APPINFO.NAME}')
    print(f'Version: {APPINFO.VERSION}')
    print(f'Created By: {APPINFO.COPYRIGHT}')

    if CurrentYear == 2021:
        print(f'Copyright © {CurrentYear} | {APPINFO.COPYRIGHT}. All rights reserved.')
        print("="*80)
    else:
        print(f'Copyright © 2021 - {CurrentYear} | {APPINFO.COPYRIGHT}. All rights reserved.')
        print("="*80)
    Salutation()

def Salutation():
    
    if Hour >= 6 and Hour < 12:
        DayPeriod = "Morning"
        print(f'Hello {APPINFO.LOCALUSERNAME}. Good {DayPeriod}! - {TimeAccess}')
        print("="*80)
    elif Hour >= 12 and Hour < 18:
        DayPeriod = "Afternoon"
        print(f'Hello {APPINFO.LOCALUSERNAME}. Good {DayPeriod}! - {TimeAccess}')
        print("="*80)
    elif Hour >= 18 and Hour != 0:
        DayPeriod = "Evening"
        print(f'Hello {APPINFO.LOCALUSERNAME}. Good {DayPeriod}! - {TimeAccess}')
        print("="*80)
    else:
        print(f'Hello {APPINFO.LOCALUSERNAME}. Nice to see you! - {TimeAccess}')
        print("="*80)
