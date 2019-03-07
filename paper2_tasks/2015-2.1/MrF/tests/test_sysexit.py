import pytest
def f():
    raise TypeError

def test_mytest():
    with pytest.raises(SystemExit):
        f()