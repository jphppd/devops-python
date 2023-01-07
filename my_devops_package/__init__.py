"""
Initialization of the module.

This file is executed once, when the module is imported. This is also true when calling the module
in command-line (see __main__.py).

This file may contain some code, whose purpose is to initialize some variables, etc.
Argument parsing, and more generally, cli interactions must be put in __main__.py though.
"""

from importlib import metadata

# __package__ is described here https://docs.python.org/3/reference/import.html#__package__
__version__ = metadata.version(__package__)

# If possible, avoid global variables. It tends to make the code messy.
COMMON_VARIABLE = "COMMON_VARIABLE_initial_value"
