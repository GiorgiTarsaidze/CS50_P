import pytest
from plates import is_valid

def main():
    test_min_max()
    test_two_letters()
    test_middle_num()
    test_zero()
    test_symbols()

def test_min_max():
    assert is_valid("AB") == True
    assert is_valid("ABC") == True
    assert is_valid("ABCD") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("QWERTYUI") == False

def test_two_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False

def test_middle_num():
    assert is_valid("CSS222") == True
    assert is_valid("CS2222") == True
    assert is_valid("CS2A2S") == False
    assert is_valid("CSS22S") == False
def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
def test_symbols():
    assert is_valid("CS.50") == False
    assert is_valid("CS 50") == False
    assert is_valid("AA 2 3") == False
    assert is_valid("CSTG 3") == False
    assert is_valid("CS!50") == False


if __name__ == "__main__":
    main()
