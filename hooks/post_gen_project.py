import os
import shutil

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
        dir_path: str = os.path.join(CUR_DIR, directoryName)
        os.mkdir(dir_path)

        with open(os.path.join(dir_path, ".gitignore"), "w") as _:
            pass


def remove_codecov(*, force: bool = False):
    """
    Removes `codecov.yml` file from the project root if Codecov is not being used
    """

    codecov_needed: bool = bool("{{ cookiecutter.use_codecov }}".lower() == "y")

    if not codecov_needed or force:
        # If Codecov is not needed, delete `codecov.yml`
        dest_path: str = os.path.join(CUR_DIR, ".codecov.yml")

        if not os.path.exists(dest_path):
            return False  # The file to delete does not exist

        os.remove(dest_path)
        return True

    return False


def remove_workflows(*, force: bool = False):
    """
    Removes the `.github` directory containing Github workflows from project root if not needed
    """

    actions_needed: bool = bool("{{ cookiecutter.use_github_actions }}".lower() == "y")

    if not actions_needed or force:
        dest_path: str = os.path.join(CUR_DIR, ".github")
        if not os.path.exists(dest_path):
            return False  # The directory to delete does not exist

        shutil.rmtree(dest_path, ignore_errors=True)

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

    config_file: str = os.path.join(CUR_DIR, ".pre-commit-config.yaml")
    workflow: str = os.path.join(CUR_DIR, ".github", "workflows", "pre-commit.yml")

    if os.path.exists(config_file):
        os.remove(config_file)

    if os.path.exists(workflow):
        os.remove(workflow)


def lincese_generator():
    """
    Generates the appropriate license for the template from the given options
    """

    # Get the selected license - the license file to be used will be the capitalized version
    # of the first word in the license name
    selected_license: str = "{{ cookiecutter.license }}"
    license_file: str = selected_license.split()[0].upper()

    source = os.path.join(CUR_DIR, "_licenses", license_file)
    destination = os.path.join(CUR_DIR, "LICENSE")

    # Move the selected license file, remove the `_licenses` directory when done
    shutil.move(source, destination)
    shutil.rmtree(os.path.join(CUR_DIR, "_licenses"), ignore_errors=True)


def remove_security_md():
    """
    Removes the `SECURITY.md` file in case the email field is empty -- if the email ID is empty,
    people cannot get in touch with project stakeholders to report vulnerabilities, making the
    `SECURITY.md` file be pointless.
    """

    should_remove: bool = bool("{{ cookiecutter.contact_email }}" == "")
    if not should_remove:
        return

    os.remove(os.path.join(CUR_DIR, "SECURITY.md"))


runners: Callable[[Optional[Any]], None] = [
    create_temp_directories,
    remove_codecov,
    remove_workflows,
    lincese_generator,
    remove_security_md,
]

for runner in runners:
    try:
        runner()
    except ValueError as e:
        print(e)
        exit(-10)
