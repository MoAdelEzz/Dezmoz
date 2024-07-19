import platform
import pip
from os import system

def import_or_install(package, download):
    try:
        __import__(package)
        print("Package (" + package + ") found importing ..." )
    except ImportError:
        print("Package (" + package + ") not found do you want to download it ? (y/n)")
        answer = input()

        if answer[0] == "y":
            print("installing .... (if failed, please try to download it using powershell or raising administration)")
            pip.main(['install', download])
            import_or_install(package, download)
        else:
            print("Exiting ...")


def initializeDependencies():
    if platform.python_version()[0] != "3":
        print("This application is only compatible with Python 3.x")
        exit(400)
    import_or_install("PySide6", "PySide6")
    import_or_install("PySide6", "PySide6-Addons")
    import_or_install("PySide6", "PySide6-Essentials")
    import_or_install("matplotlib", "matplotlib")
    import_or_install("re", "regex")


def runApp():
    exe_path = "./__init__.py"
    system(f"python {exe_path}")


initializeDependencies()
runApp()