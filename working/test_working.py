from working import convert
import pytest

def main():
    test_convert()

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 AM to 4 PM") == "10:00 to 16:00"
    assert convert("9:30 AM to 5 PM") == "09:30 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("11 AM to 3:00 PM") == "11:00 to 15:00"
    assert convert("10:15 AM to 2 PM") == "10:15 to 14:00"

    try:
        convert("9:60 AM to 5:60 PM")
        raise AssertionError
    except ValueError:
        pass
    try:
        convert("9 AM - 5 PM")
        raise AssertionError
    except ValueError:
        pass


if __name__ == "__main__":
    main()
