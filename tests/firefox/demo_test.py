import pytest

from helpers.image_search import *


# Example of test that might throw errors that we want to ignore
# https://docs.pytest.org/en/2.9.0/skipping.html
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_raises():
    assert 1 == 1
    error = 9 / 0


# Example of test with debug
# https://docs.pytest.org/en/2.9.0/usage.html?highlight=pdb
def test_with_debug():
    string = 'test'
    # pytest.set_trace()


def test_confirm_launch():
    exists('reload.png')
