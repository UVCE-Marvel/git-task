"""testing functions"""
from main import add

def test_add():
    """testing add function"""
    assert add(2,3) == 5, "Expected 5"
    assert add(0, 42) == 42, "Expected 42"
    assert add(-1, 1) == 0, "Expected 0"

test_add()