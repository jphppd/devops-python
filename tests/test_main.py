"""Run some tests."""

import pytest

from my_devops_package import app


def test_dummy():
    """Run a simple assert."""
    assert True


def test_resource():
    """Assert the content of the resource."""
    assert app.JSON_RESOURCE == {"key1": "value1", "key2": ["value2", "value3"]}


def test_fail_resource():
    """Anti-assert the content of the resource."""
    with pytest.raises(AssertionError):
        assert app.JSON_RESOURCE == {"key1": "value1", "key2": "value1"}
