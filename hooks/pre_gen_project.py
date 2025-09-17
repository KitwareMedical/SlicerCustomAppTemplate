import re
import sys

APP_NAME_REGEX = r"^[a-zA-Z0-9]+$"

app_name = "{{ cookiecutter.app_name }}"

if not re.match(APP_NAME_REGEX, app_name):
    print(
        f"ERROR: {app_name} is not a valid app name. "
        "Only alphanumeric characters are allowed."
    )

    # exits with status 1 to indicate failure
    sys.exit(1)
