__config_version__ = 1

GLOBALS = {
    "serializer": "{{major}}.{{minor}}.{{patch}}",
}

FILES = ["setup.py", "kedro_static_viz/__init__.py", "kedro_static_viz/cli.py"]

VERSION = ["major", "minor", "patch"]

# VCS = {
#     'name': 'git',
#     'commit_message': (
#         "Version updated from {{ current_version }}"
#         " to {{ new_version }}")
# }
