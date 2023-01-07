"""Create the distributions."""

from setuptools import setup


def prereleaser_set_commit_msg(data):
    """Override the default commit message for prerelease."""
    data["commit_msg"] = "[^] Preparing release: %(new_version)s"


def postrealeaser_set_commit_msg(data):
    """Override the default commit message for postrelease."""
    data["commit_msg"] = "[^] Back to development: %(new_version)s"


if __name__ == "__main__":
    setup()
