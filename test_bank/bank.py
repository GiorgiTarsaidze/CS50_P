def main():
    greeting = input("Greeting: ")
    greetingv = value(greeting)
    print(f"${greetingv}")

def value(greeting):
    #store our greeting input, then remove the spacebars and make it lower-case
    greeting = greeting.strip().lower()
    if "hello" in greeting:
        return 0

    #if there is letter "h" in first position in our greeting, then print $20
    elif "h" == greeting[0]:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()