import validators

def main():
    print(response(input("What's your email address? ")))

def response(a):
    match = bool(validators.email(a))
    if match == True:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()