from os import mkdir, remove
from os.path import join, exists
from shutil import rmtree
from pathlib import Path
from sys import exit
from typing import Callable, List, Optional, Any

# Contains path to the project directory - i.e. {{cookiecutter.project_name}}
CUR_DIR = Path.cwd().absolute()


# List of temporary directories, each directory will also contain an empty `.gitignore` file
temp_directories: List[str] = [
    "bin",
    "coverage",
]


def create_temp_directories():
    """
    Creates an empty directory for `directories`, places a gitignore file inside them
    """

    for directoryName in temp_directories:
        dir_path: str = join(CUR_DIR, directoryName)
        mkdir(dir_path)

        with open(join(dir_path, ".gitignore"), "w") as _:
            pass


def remove_codecov(*, force: bool = False):
    """
    Removes `codecov.yml` file from the project root if Codecov is not being used
    """

    codecov_needed: bool = bool("{{ cookiecutter.use_codecov }}".lower() == "y")

    if not codecov_needed or force:
        # If Codecov is not needed, delete `codecov.yml`
        dest_path: str = join(CUR_DIR, ".codecov.yml")

        if not exists(dest_path):
            return False  # The file to delete does not exist

        remove(dest_path)
        return True

    return False


def remove_workflows(*, force: bool = False):
    """
    Removes the `.github` directory containing Github workflows from project root if not needed
    """

    actions_needed: bool = bool("{{ cookiecutter.use_github_actions }}".lower() == "y")

    if not actions_needed or force:
        dest_path: str = join(CUR_DIR, ".github")
        if not exists(dest_path):
            return False  # The directory to delete does not exist

        rmtree(dest_path, ignore_errors=True)

        # Since workflows are to be removed, remove `codecov.yml` as well
        remove_codecov(force=True)


def precommit_handler():
    """
    If pre-commit is not to be used, removes pre-commit configuration file, and the Github workflow
    for the same
    """

    use_precommit: bool = bool("{{ cookiecutter.use_precommit }}".lower() == "y")
    if use_precommit:
        return

    config_file: str = join(CUR_DIR, ".pre-commit-config.yaml")
    workflow: str = join(CUR_DIR, ".github", "workflows", "pre-commit.yml")

    if exists(config_file):
        remove(config_file)

    if exists(workflow):
        remove(workflow)


runners: Callable[[Optional[Any]], None] = [
    create_temp_directories,
    remove_codecov,
    remove_workflows,
]

for runner in runners:
    try:
        runner()
    except ValueError as e:
        print(e)
        exit(-10)
