from main import add

def test1():
    assert add(2,3) == 5

def test2():
    assert add(0,42) == 42

def test3():
    assert add(-1,1) == 0
