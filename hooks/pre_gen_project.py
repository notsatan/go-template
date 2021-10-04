from re import match
from sys import exit
from typing import Callable

# Regex to determine if a module name is valid. Conditions to pass;
#   - First letter should be lower case alphabet
#   - Should consist of alphabets and/or hyphen ONLY
#   - Should have length between [3, 11] characters (inclusive)
MODULE_NAME_REGEX: str = r"^[a-z][a-zA-Z\-]{2,10}$"

# Name of the module from Cookiecutter configs
module_name = r"{{ cookiecutter.module_name }}"


def validate_module_name():
    """
    Raises `ValueError` if module name is invalid. Uses `MODULE_NAME_REGEX` to validate
    """

    if not match(MODULE_NAME_REGEX, module_name):
        raise ValueError(f"Error: Invalid module name: `{module_name}`")


validators: Callable[[], None] = [
    validate_module_name,
]

for validator in validators:
    try:
        validator()
    except ValueError as e:
        print(e)
        exit(-10)
