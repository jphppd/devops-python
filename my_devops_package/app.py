"""Simple app example."""

import json
import logging
from importlib import resources

import yaml

import my_devops_package

# Get the absolute path of the resource
JSON_PATH = resources.files(__package__) / "data" / "data.json"

# Get the content of the specified resource as a bytes object
RESOURCE_BYTES = JSON_PATH.read_bytes()
JSON_RESOURCE = json.loads(RESOURCE_BYTES.decode())


def print_yaml():
    """Print yaml version of JSON_RESOURCE."""
    logging.info("__package__: %s", __package__)
    logging.info("__name__: %s", __name__)
    logging.info("Printing the resource:")
    logging.info("%s", yaml.dump(JSON_RESOURCE))
    my_devops_package.COMMON_VARIABLE = "COMMON_VARIABLE_was_modified_by_app"
