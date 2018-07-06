import pytest

from helpers.image_search.image_search import *


# Example of test that might throw errors that we want to ignore
# https://docs.pytest.org/en/2.9.0/skipping.html
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_raises():
    assert 1 == 1
    zero_division = 9 / 0


# Example of test with debug
# https://docs.pytest.org/en/2.9.0/usage.html?highlight=pdb
def test_with_debug():
    # pytest.set_trace()
    pass


def test_confirm_launch():
    time.sleep(2)
    find('reload.png')
