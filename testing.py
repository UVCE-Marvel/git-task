"""testing functions"""
from main import add

def test_add():
    """testing add function"""
    assert add(2,3) == 5,"should be 5"
    assert add(0, 42) == 42,"should be 42"
    assert add(-1, 1) == 0,"Should be 0"
