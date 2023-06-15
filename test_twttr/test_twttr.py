import pytest
from traki.twttr import shorten

def main():
    test_words()

def test_words():
    assert shorten("Twitter") == "Twttr"
    assert shorten("CATO") == "CT"
    assert shorten("cAtO") == "ct"
    assert shorten("cATo") == "cT"
    assert shorten("343132") == "343132"
    assert shorten("What's up, yo") == "Wht's p, y"

def test_upper():
    assert shorten("CATOT").isupper()
    assert shorten("CATATO").isupper()

if __name__ == "__main__":
    main()