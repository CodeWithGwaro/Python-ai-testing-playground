def divide(a, b):
    return a / b

def test_divide_by_zero():
    import pytest
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)