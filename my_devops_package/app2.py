"""Simple cross-import example."""

from devops_package.app import JSON_RESOURCE, JSON_PATH


def print_resource():
    """Print the imported JSON_RESOURCE."""
    print(__package__)
    print(JSON_RESOURCE)
    print(JSON_PATH)
