import os
import re
import shutil

import textwrap
from pathlib import Path
from sys import exit
from typing import Callable, List, Optional, Any

# Contains path to the project directory - i.e. {{cookiecutter.project_name.strip()}}
CUR_DIR = Path.cwd().absolute()


# List of temporary directories, each directory will also contain an empty `.gitignore` file
temp_directories: List[str] = [
    "bin",
    "coverage",
]


def lincese_generator():
    """
    Generates the appropriate license for the template from the given options
    """

    # Get the selected license - the license file to be used will be the capitalized version
    # of the first word in the license name
    selected_license: str = "{{ cookiecutter.license }}".upper()
    license_file: str = re.findall(r"^[a-zA-Z]+", selected_license)[0]

    source = os.path.join(CUR_DIR, "_licenses", license_file)
    destination = os.path.join(CUR_DIR, "LICENSE")

    # Move the selected license file, remove the `_licenses` directory when done
    shutil.move(source, destination)
    shutil.rmtree(os.path.join(CUR_DIR, "_licenses"), ignore_errors=True)


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
        dest_path: str = os.path.join(CUR_DIR, "codecov.yml")

        if not os.path.exists(dest_path):
            return False  # The file to delete does not exist

        os.remove(dest_path)
        return True

    return False


def disable_github_features(*, force: bool = False):
    """
    Removes the `.github` directory containing Github workflows from project root if not needed.
    Additionally, goes on to remove any other file/directory that would be specific to Github
    """

    github_features_needed: bool = bool(
        "{{ cookiecutter.github_specific_features }}".lower() == "y"
    )

    if github_features_needed and not force:
        # If Github-specific features are needed, and the action is not forced, skip
        return

    dest_path: str = os.path.join(CUR_DIR, ".github")
    if not os.path.exists(dest_path):
        return False  # The directory to delete does not exist

    shutil.rmtree(dest_path, ignore_errors=True)

    # Since workflows are to be removed, remove `codecov.yml` as well
    remove_codecov(force=True)


def remove_precommit():
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


def check_email_provided():
    """
    Checks if the user has provided an email while generating the template

    Removes the `SECURITY.md` and `CODE_OF_CONDUCT.md` file in case the email field is empty -- if
    the email ID is empty, people cannot get in touch with project stakeholders to report, making
    the file(s) be pointless.
    """

    should_remove: bool = bool("{{ cookiecutter.contact_email }}" == "")
    if not should_remove:
        return

    # List of files to be removed
    files: List[str] = ["SECURITY.md", "CODE_OF_CONDUCT.md"]
    for f in files:
        deletable_file = os.path.join(CUR_DIR, f)
        if not os.path.exists(path=deletable_file):
            continue

        os.remove(deletable_file)


def print_final_instructions():
    """
    Simply prints final instructions for users to follow once they generate a project
    using this template!
    """

    message = """
    ====================================================================================

    Your project `{{ cookiecutter.project_name.strip() }}` is ready!

    It is suggested to go through the generated `README` for detailed instructions on
    how to use the tools that come with `go-template`! The following is a *brief*
    overview of steps to push code to remote.

    1) Move to project directory, and initialize a git repository:
        $ cd {{ cookiecutter.project_name.strip() }} && git init

    2) Run codestyle:
        $ make codestyle

    3) Run linters and codestyle checkers
        $ make lint

    4) Run the complete test-suite:
        $ make test

    7) Upload initial code to git:
        $ git add -a
        $ git commit -m "Initial commit!"
        $ git remote add origin https://{{ cookiecutter.go_module_path.strip('/') }}.git
        $ git push -u origin --all

    If you have any suggestions, or encounter any issue, please raise an issue;
        https://github.com/notsatan/go-template
    """

    print(textwrap.dedent(message))


runners: Callable[[Optional[Any]], None] = [
    lincese_generator,
    create_temp_directories,
    remove_codecov,
    disable_github_features,
    remove_precommit,
    check_email_provided,
    print_final_instructions,
]

for runner in runners:
    try:
        runner()
    except ValueError as e:
        print(e)
        exit(-10)
