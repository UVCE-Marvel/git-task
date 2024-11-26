"""testing functions"""
from updated import add

def test_add():
    """testing add function"""
    assert add(2,3) == 5
    assert add(0, 42) == 42
    assert add(-1, 1) == 0
print(add(3,5))