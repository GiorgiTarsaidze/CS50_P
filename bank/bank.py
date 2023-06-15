#store our greeting input, then remove the spacebars and make it lower-case
greeting = input("Greeting: ").strip().lower()
if "hello" in greeting:
    print("$0")

#if there is letter "h" in first position in our greeting, then print $20
elif "h" == greeting[0]:
    print("$20")
else:
    print("$100")