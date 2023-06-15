from numb3rs import validate
import pytest

def main():
    test_false_check()
    test_true_check()

def test_false_check():
    assert validate(r"255.255.255.256") == False
    assert validate(r"256.3455.255432.432256") == False
    assert validate(r"-1.235.25.2") == False
    assert validate(r"2434.4355.-255.256") == False
    assert validate(r"cat.dog.cat.dog") == False
    assert validate(r"1.1.1") == False
    assert validate(r"1.1.1.") == False
    assert validate(r"1.1") == False
def test_true_check():
    assert validate(r"255.255.254.0") == True
    assert validate(r"168.125.2.1") == True
    assert validate(r"255.255.0.0") == True
    assert validate(r"232.23.3.2") == True
    assert validate(r"0.0.0.0") == True

if __name__ == "__main__":
    main()