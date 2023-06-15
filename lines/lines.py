import sys


# main function measuring length of arguments
def main():
    n = len(sys.argv)
    if n < 2:
        sys.exit("Too few command-line arguments")
    elif n > 2:
        sys.exit("Too many command-line arguments")
    elif n == 2:
# if there is one extra argument we transfer it to counter function
        x = sys.argv[1]
        print(counter(x))


def counter(x):
    if x.endswith(".py"):
        try:
            with open(x) as file:
                i = 0
# first, we strip our lines and add 1 for each line in our file
                for line in file:
                    line = line.lstrip()
                    i += 1
# For every line that is empty or starts with # we subrtact 1
                    if line.startswith("#"):
                        i -= 1
                    elif line.strip() == "":
                        i -= 1
                return i
        except FileNotFoundError:
            sys.exit("File does not exist")
# if name of the file does not end with '.py', we exit via sys
    else:
        sys.exit("Not a Python file")

main()