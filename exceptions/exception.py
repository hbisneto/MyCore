"""
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
"""
## Exceptions File
## This file contains events that's raised when the program must to stop

class Raise:
  def major_version(self, current_version, target_version):
    raise Exception(f'>> You cannot run the application because it requires Python {target_version} or later. [Current Version: {current_version}]')

  def minor_version(self, current_version, target_version):
    print(f'\n{"="*80}')
    print("[ !!! ]: PYBRIDGE - WARNING:")
    print('=' * 80)
    print(f'>> Your appication targets an old version of Python')
    print('You may get errors during the process')
    print('=' * 80)
    print(f'- Current Version: {current_version}')
    print(f'- Target Version: {target_version}')
    print(f'>> You can change `Requirements.py` on `system` Module')
    print('=' * 80)
        
  def __init__(self, exctype):
    self.exctype = exctype

  def file_exists(self):
    raise Exception(f'{self.exctype} The file already exists')
  
  def directory_exists(self):
    raise Exception(f'{self.exctype} The directory already exists')
  
  def project_exists(self):
    raise Exception(f'{self.exctype} The project already exists')
  
  def import_lib(self):
    raise RuntimeError(">> Could not import library: Check if the libraries are installed and run the program again.")

  def input_format(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} INVALID INPUT')
    print("=" * 80)
    print(">> Your input is not valid: Check your input and try again")
    print("=" * 80)
  
  def programq_quit(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} PYBRIDGE HAS QUIT!')
    print("=" * 80)
    print(f'>> The program has been closed and couldn`t be restored.')
    print('>> Run the program again!')
    print("=" * 80)

  def invalid_option(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} INVALID OPTION')
    print("=" * 80)
    print(f'>> You typed an invalid option.')
    print("=" * 80)

  def projects_load_fail(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} PROJECT LOADING FAILED!')
    print("=" * 80)
    print(f'>> ERROR: Couldn`t load projects...')
    print("=" * 80)

  def backup_fail(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} BACKUP CREATION FAILED!')
    print("=" * 80)
    print("*" * 80)
    print(f'>> PyBridge could not create backup for your projects folder')
    print(f'>> Try again later.')
    print("*" * 80)

  def compress_backup_fail(self):
    print()
    print("=" * 80)
    print(f'{self.exctype} COMPRESSED FILE CREATION FAILED!')
    print("=" * 80)
    print("*" * 80)
    print(f'>> PyBridge could not create a compressed file from your backup')
    print(f'>> Try again later.')
    print("*" * 80)

Throw = Raise("")

# Throw.CompressBackupFail() # REMOVE THIS LINE