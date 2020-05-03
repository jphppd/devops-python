"""Package devops entry point."""

from pkg_resources import get_distribution, DistributionNotFound

try:
    # The name must be the same as the value of the "name" key in the setup.py file
    __version__ = get_distribution(__package__).version
except DistributionNotFound:
    pass
