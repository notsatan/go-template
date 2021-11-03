import re

from sys import exit
from typing import Callable, List, Any, Optional


def is_module_hosted_on_github():
    """
    Ensures if user has chosen to enable github-specific features, the module path
    should belong to Github
    """

    # Regex pattern to validate module name - might need some tweaks
    pattern = r"^github.com\/[a-zA-Z0-9\-]+\/[a-zA-Z0-9\-]+\/?$"

    # If the user has not opted for Github-specific features, skip
    perform_check: bool = bool(
        "{{ cookiecutter.github_specific_features }}".lower() == "y"
    )

    if not perform_check:
        return

    if not re.match(pattern, "{{ cookiecutter.go_module_path }}"):
        raise ValueError(
            "Attempt to enable Github-specific features when module path does not "
            + "belong to github"
        )


validators: Callable[[Optional[Any]], None] = [
    is_module_hosted_on_github,
]

for validator in validators:
    try:
        validator()
    except Exception as e:
        print(f"\n\nRan into exception while running validator: `{validator.__name__}`")
        print(f"Stacktrace: `{type(e).__name__}: {e}`")
        print(
            f"""  \
\n\ngo-template is still under development, if you feel that the error is incorrect, \
you are encouraged to raise an issue at: \n\thttps://github.com/notsatan/go-template
"""
        )

        exit(-10)
