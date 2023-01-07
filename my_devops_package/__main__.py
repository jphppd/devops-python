"""
Entry point of the module.

This file is meant to be the entry point of the package:
    python -m my_devops_package arg1 arg2 ...
The -m argument instructs python to look for, and execute, __main__.py in my_devops_package.

In order to keep the code structured and maintainable, handle your (command line) arguments in
this file only. Try to pass explicit arguments in the subsequent function calls rather, than the
raw result of parse_args(). Conversely, try to keep explicit argument names in your functions:
testing will be all the easier.
"""

import argparse
import json
import logging
import sys
from pathlib import Path

import my_devops_package
from my_devops_package.app import print_yaml
from my_devops_package.app2 import print_resource
from my_devops_package.utils.init_logging import init_logging
from my_other_package import HELLO_FROM_OTHER_PACKAGE


def parse_args():
    """Parse command line arguments.

    In this example, the package is expected to be called this way:
        python -m my_devops_package --config <path_to_config>
    and the configuration is a json file.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config", default=Path("config.json"), help="path to the configuration file", type=Path
    )
    args = parser.parse_args()

    with args.config.open() as config_fh:
        config = json.load(config_fh)
    return config


def main():
    """Entry point of the package."""
    init_logging("package.log")
    logging.info("COMMON_VARIABLE: %s", my_devops_package.COMMON_VARIABLE)

    print_yaml()
    print_resource()

    config = parse_args()
    logging.info("__package__: %s", __package__)
    logging.info("__name__: %s", __name__)
    logging.info("config: %s", config)
    logging.info("COMMON_VARIABLE: %s", my_devops_package.COMMON_VARIABLE)

    logging.info("HELLO_FROM_OTHER_PACKAGE: %s", HELLO_FROM_OTHER_PACKAGE)

    an_error_occurred = False

    if an_error_occurred:
        # A non-zero return code typically indicates an error.
        return 1

    # A zero return code indicates that everything went fine.
    return 0


if __name__ == "__main__":
    sys.exit(main())
