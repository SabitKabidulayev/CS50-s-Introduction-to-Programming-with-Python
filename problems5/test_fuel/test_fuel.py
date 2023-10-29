import pytest
from fuel import convert, gauge

def test_value_error():
    with pytest.raises(ValueError):
        convert("10/3")
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_correct_input():
    assert convert("1/4") == 25 and gauge(25) == "25%"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_gauge_empty():
    assert gauge(1) == "E"
    assert gauge(0.5) == "E"
    assert gauge(0) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(99.9) == "F"

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"