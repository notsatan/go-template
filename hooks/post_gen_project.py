### Simply create the `tmp`, `bin` and `coverage` directories

from os import mkdir, remove
from os.path import join
from pathlib import Path
from sys import exit
from typing import Callable, List

# Contains path to the project directory - i.e. {{cookiecutter.project_name}}
CUR_DIR = Path.cwd().absolute()


# List of temporary directories, each directory will also contain an empty `.gitignore` file
temp_directories: List[str] = [
    "bin",
    "coverage",
    "tmp",
]


def remove_codecov():
    """
    Removes `codecov.yml` file from the project root if Codecov is not being used
    """

    codecov_needed: bool = bool("{{ cookiecutter.use_codecov }}".lower() == "y")

    if not codecov_needed:
        # If Codecov is not needed, delete `codecov.yml`
        remove("codecov.yml")


def create_temp_directories():
    """
    Creates an empty directory for `directories`, places a gitignore file inside them
    """

    for directoryName in temp_directories:
        dir_path: str = join(CUR_DIR, directoryName)
        mkdir(dir_path)

        with open(join(dir_path, ".gitignore"), "w") as _:
            pass


runners: Callable[[], None] = [
    create_temp_directories,
    remove_codecov,
]

for runner in runners:
    try:
        runner()
    except ValueError as e:
        print(e)
        exit(-10)
