import re

def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower().strip()
    pattern = r'\bum\b'
    match = re.findall(pattern,s)
    return len(match)


if __name__ == "__main__":
    main()