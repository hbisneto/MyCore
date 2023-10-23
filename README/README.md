# MyCore 1.8

This version is designed to speed up access to project information.
Now, with the unification of the FileSystem libraries for macOS, Windows and Linux in a single file, just use `from system import FileSystem`. This simplifies the code, making it cleaner and more efficient. Additionally, new libraries have been added. These enhancements further expand the functionality and versatility of the system.

This version brought a flatter structure, with many libraries now in the root directory. Additionally, the `system` directory has been expanded with new files such as the new `Core.py`, `File.py`, `Requirements.py`, and `[Services].py`.

## Improvements

- Improvements in PyBridge CLI
- **.gitignore:** Added more files to ignore
- **MyCore Map:** Enhanced functionalities including more libraries to the project.
- **mac module:** Another text here
- **Exceptions:** Another text here
- Some text here

Version 1.7:

- App.py: Changes in Menu
- Added APPINFO.py file
- Added CLI.py file
- FileSystem: Removed `from system import APPINFO` and added `import APPINFO` instead.
- Added Menu.py
- Changes in README.md
- Exceptions: Each function will run after a new line
- Mac.py: Removed `from system import SplashScreen` and added `APPINFO.loadSplashScreen()` on `Mac()` function
- Requirements: Added a new line when running `InstallDependencies()` function

This update removes `APPINFO.py` and `SplashScreen.py` from `system` module.

## MyCore Map

```
.
├── __init__.py
├── .gitignore
├── app.py
├── cli.py
├── info.py
│ 
├── exceptions
│ ├── exception.py
│ 
├── system
│ ├── core.py
│ ├── downloads.py
│ ├── filesystem.py
│ ├── logs.py
│ ├── menus.py
│ ├── requirements.py
│ 
├── linux
│ ├── linux.py
│ 
├── mac
│ ├── mac.py
│ 
├── windows
│ ├── windows.py
│ 
└── README.md
```