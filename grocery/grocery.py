# First, we create an empty dictionary, were we are going to store our items
products = {}

while True:
    try:
#Here we ask user for input and store it in x variable
        x = input()
# Cheking inf our input is already in the dictionary and adding second value +1 to it
        if x in products:
            products[x]+=1
# If our input is not in dicitionary it automatically gets value = 1
        else:
            products[x]=1
# After pressing ctrl d we print a new line, start a for loop
    except EOFError:
        print()
# Here, we sort our product list in alphabetical order
        for i in sorted(products):
# Make them upper-case and assign variable b as a count to each of them
            a = i.upper()
            b = products[i]
# Lastly, we foramt our count variable b and products, print it and break the loop
            print(f"{b} {a}")
        break
