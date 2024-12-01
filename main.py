import os
from pathlib import Path

PIP_INSTALL_CMD = "pip install"

BEGIN_LIBS = [
    "pyside6",
    "py7zr",
]

MC_RUN_LIB = "portablemc"

LAUNCHER_PATH = "C:\\FLauncher"
LAUNCHER_GITHUB_URL = "https://github.com/MrFufl4ik/FLauncher.git"


def is_windows():
    if os.name == "nt":
        return True
    elif os.name == 'posix':
        return False


def install_python_libs(libs: list, user = False):
    if not user:
        for lib in libs:
            print(f"Устанавливаю библиотеку python: {lib}")
            os.system(f"{PIP_INSTALL_CMD} {lib}")
            print("Успешно")
    else:
        for lib in libs:
            print(f"Устанавливаю библиотеку python: {lib}")
            os.system(f"{PIP_INSTALL_CMD} --user {lib}[certifi]")
            print("Успешно")


def git_clone(path: str):
    os.system(f"git clone {LAUNCHER_GITHUB_URL} {path}")


def win_set_path(path: str):
    os.system(f"fsetx /M PATH \"%PATH%;{path}\"");


def win_install():
    print(f"Начало установки для: {os.name}")
    install_python_libs(BEGIN_LIBS)
    print("Начальные библиотеки установлены...")

    install_python_libs([MC_RUN_LIB],True)
    folder_path = Path(f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Python")
    folders = [f for f in folder_path.iterdir() if f.is_dir()]
    folder_names = [str(folder) for folder in folders]

    win_set_path(f"{folder_path}\\{folder_names[0]}\\Scripts")
    if not os.path.exists(LAUNCHER_PATH):
        os.makedirs(LAUNCHER_PATH)
        git_clone(LAUNCHER_PATH)


def main():
    if is_windows():
        win_install()
    else:
        print(f"Пока не поддерживается установка под: {os.name}")


if __name__ == "__main__": main()