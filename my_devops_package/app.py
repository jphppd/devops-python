"""Simple app example."""

import json
from pkg_resources import resource_string, resource_filename

import yaml

# Get the absolute path of the resource
JSON_PATH = resource_filename(__name__, 'data/data.json')

# Get the content of the specified resource
RESOURCE_BYTES = resource_string(__name__, 'data/data.json')
JSON_RESOURCE = json.loads(RESOURCE_BYTES.decode())


def print_yaml():
    """Print yaml version of JSON_RESOURCE."""
    print(yaml.dump(JSON_RESOURCE))
