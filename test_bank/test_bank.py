import bank

def main():
    test_hello()


def test_hello():
    hello = ["Hello","HeLlo", "Hello , how are you?", "Hello, what's up?", "Hello 123"]
    for word in hello:
        assert bank.value(word) == 0
def test_h():
    h = ["Hey","How are you", "Hey yo", "HEY MAN", "Hi", "Holla"]
    for word in h:
        assert bank.value(word) == 20
def test_elses():
    elses = ["Yo", "Salute!", "What's up?", "123", "Gamarjoba!"]
    for word in elses:
        assert bank.value(word) == 100

if __name__ == "__main__":
    main()