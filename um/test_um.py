from um import count

def main():
    test_count()

def test_count():
    assert count("Hello, um, my name is George, um") == 2
    assert count("Hi there") == 0
    assert count("Um, UM, um, UMMM") == 3
    assert count("1   um    1") == 1
    assert count("very, um, interesting, um, um um") == 4
    assert count("um, cool, um") == 2

if __name__ == "__main__":
    main()