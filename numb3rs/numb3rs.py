import re
# *We didn't use the sys library
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # This is a pattern which checks if there is a digit besides the dots in given "ip" argument
    if re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",ip):
        # Here, we are spliting the numbers into a list
        numbers = ip.split(".")
        # Then, we are checking for a range of each given number in the list (if it's in between 0 and 255)
        for i in numbers:
            if int(i) < 0 or int(i) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()