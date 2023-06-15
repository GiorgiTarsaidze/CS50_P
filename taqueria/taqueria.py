menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#Define our total $ with variable
total = 0
#Whole code is in a WHILE loop
while True:
    try:
# X is an item that our customer searchs for
        x = input("Item: ").title()
        if x in menu:
# We look up our x in the menu dictionary
            total += menu[x]
            print("Total: $", end="")
            print("{:.2f}".format(total))
# We except line breaks and that will break our loop

    except EOFError:
        print()
        break