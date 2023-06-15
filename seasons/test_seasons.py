import pytest
from seasons import format_check, date_to_minutes, minutes_to_text
from datetime import date

def main():
    test_format()
    test_minutes()
    test_text()

def test_format():
    with pytest.raises(SystemExit):
        format_check("20242-08-01")
        format_check("2352-18-01")
        format_check("1303-28-01")
        format_check("1999-08-33")
        format_check("20004-31-35")


def test_minutes():
    input_date = date.fromisoformat("2000-01-01")
    assert date_to_minutes(input_date) == 12258720

    with pytest.raises(SystemExit):
        input_date2 = date.fromisoformat("2026-01-01")
        date_to_minutes(input_date2)

def test_text():
    assert minutes_to_text(200) == "two hundred"
    assert minutes_to_text(1000) == "one thousand"
    assert minutes_to_text(2001) == "two thousand one"
    assert minutes_to_text(3021) == "three thousand twenty-one"
    assert minutes_to_text(1242) == "one thousand, two hundred forty-two"

if __name__ == "__main__":
    main()