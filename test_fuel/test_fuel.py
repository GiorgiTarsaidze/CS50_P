from fuel import convert,gauge
import pytest

def main():
    test_convert()
    test_gauge()
    test_zero_division()
    test_value_error()
    test_value_error_2

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/8") == 12
    assert convert("1/1") == 100
    assert convert("1/100") == 1
    assert convert("2/4") == 50

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(12) == "12%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("2/0")
        convert("4/0")
def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("a/b")
        convert(" ")
        convert("gdgro fsd")
def test_value_error_2():
    with pytest.raises(ValueError):
        convert("15/3")
        convert("2/1")
        convert("6/3")


if __name__ == "__main__":
    main()