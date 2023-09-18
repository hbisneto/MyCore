# README

Version 1.7:

- .gitignore: Added more files to ignore
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