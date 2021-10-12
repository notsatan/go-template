from re import match
from sys import exit
from typing import Callable


def validate_module_name():
    """
    Raises `ValueError` if module name is invalid. Uses `MODULE_NAME_REGEX` to validate
    """

    # Regex to determine if a module name is valid. Conditions to pass;
    #   - First letter should be lower case alphabet
    #   - Should consist of alphabets, numbers, hyphen, underscores, forward-slash, and period ONLY
    MODULE_NAME_REGEX: str = r"^[a-z][a-zA-Z0-9\./_\-]+$"

    # Name of the module from Cookiecutter configs
    module_path = r"{{ cookiecutter.go_module_path }}"

    if not match(MODULE_NAME_REGEX, module_path):
        raise ValueError(f"Error: Invalid module name: `{module_path}`")


validators: Callable[[], None] = [
    validate_module_name,
]

for validator in validators:
    try:
        validator()
    except ValueError as e:
        print(e)
        exit(-10)
