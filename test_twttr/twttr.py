def main():
    x = shorten(input("Input: ").strip())
    print(f"Output: {x}")


def shorten(word):
    result = ""
    for letter in word:
        if letter in ['a','A','e','E','i','I','o','O','u','U']:
            continue
        else:
            result += letter
    return result


if __name__ == "__main__":
    main()