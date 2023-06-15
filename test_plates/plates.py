def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #Using isalpha to check if our string (first two letters) is made out of alphabetic letters
    if s[0:2].isalpha() == False:
        return False

    #Here, we are measuring the length of our plate. Which is not allowed to be bigger than 6 and less than 2
    if len(s) <2 or len(s) >6:
        return False

    #Doesnt start with a zero
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1
    #Numbers in the middle

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                if not s[i:].isdigit():
                    return False


    #No periods, spaces, or punctuation marks are allowed
    for _ in s:
        if _ in [","," ","!","?","."]:
            return False

    return True


if __name__ == "__main__":
    main()