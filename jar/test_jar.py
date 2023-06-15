import pytest
from jar import Jar

def test_init():
    jar = Jar()

    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    obj = Jar()
    with pytest.raises(ValueError):
        obj.deposit(13)
        obj.deposit(14)
        obj.deposit(15)
        obj.deposit(26)
    assert obj.deposit(4) == 4
    assert obj.deposit(6) == 10
    assert obj.deposit(1) == 11


def test_withdraw():
    obj = Jar()
    obj.deposit(10)
    with pytest.raises(ValueError):
        obj.withdraw(13)
        obj.withdraw(14)
        obj.withdraw(15)
        obj.withdraw(26)
    assert obj.withdraw(4) == 6
    assert obj.withdraw(5) == 1
    assert obj.withdraw(1) == 0
