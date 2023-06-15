import random as r


def main():
    count = 0
    level = get_level()
    for i in range(10):
        x, y = generate_integer(level)
        fail = 0
        while True:
            try:
                result = int(input(f"{x} + {y} = "))
                if result == x + y:
                    count += 1
                    break
                else:
                    print("EEE")
                    fail += 1
                    if fail == 3:
                        correct = x + y
                        print(f"x + y = {correct}")
                        break
            except ValueError:
                print("EEE")
                pass
        print(count)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                continue
        except:
            pass


def generate_integer(level):
    if level == 1:
        x = r.randint(0, 9)
        y = r.randint(0, 9)
    elif level == 2:
        x = r.randint(10, 99)
        y = r.randint(10, 99)
    else:
        x = r.randint(100, 999)
        y = r.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()
