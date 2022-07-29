import pytest
import utils


def test_t1():
    print("This is t1")
    assert 1 == 1

def test_t2():
    print("This is t2")
    assert 2 == 2

def test_t3():
    result = utils.add(1, 2)
    assert result == 3
