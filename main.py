import os

PIP_INSTALL_CMD = "pip install"

BEGIN_LIBS = [
    "pyside6",
    "py7zr",
]

MC_RUN_LIB = "--user portablemc[certifi]"

LAUNCHER_PATH = "C:\\FLauncher"
LAUNCHER_GITHUB_URL = "https://github.com/MrFufl4ik/FLauncher.git"


def is_windows():
    if os.name == "nt":
        return True
    elif os.name == 'posix':
        return False


def install_python_libs(libs: list):
    for lib in libs:
        print(f"Устанавливаю библиотеку python: {lib}")
        os.system(f"{PIP_INSTALL_CMD} {lib}")
        print("Успешно")


def git_clone(path: str):
    os.system(f"git clone {LAUNCHER_GITHUB_URL} {path}")


def win_set_path(path: str):
    os.system(f"setx PATH %PATH%;{path}");


def win_install():
    print(f"Начало установки для: {os.name}")
    install_python_libs(BEGIN_LIBS)
    print("Начальные библиотеки установлены...")
    install_python_libs([MC_RUN_LIB])
    win_set_path(f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Python\\Python312\\Scripts")
    os.makedirs(LAUNCHER_PATH)
    git_clone(LAUNCHER_PATH)


def main():
    if is_windows():
        win_install()
    else:
        print(f"Пока не поддерживается установка под: {os.name}")


if __name__ == "__main__": main()