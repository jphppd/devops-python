"""Simple cross-import example."""

import logging

from my_devops_package.app import JSON_PATH, JSON_RESOURCE


def print_resource():
    """Print the imported JSON_RESOURCE."""
    logging.info("__package__: %s", __package__)
    logging.info("__name__: %s", __name__)
    logging.info("JSON_RESOURCE: %s", JSON_RESOURCE)
    logging.info("JSON_PATH: %s", JSON_PATH)
