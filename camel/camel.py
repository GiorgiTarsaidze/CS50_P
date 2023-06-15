#Lets create a main fucntion which will store a variable called question with out input for camel case
#Next we print out snake case and transfer our value to another function called snake_case
def main():
    question = input("camelCase: ")
    print("snake_case: ", end="")
    snake_case(question)

def snake_case(n):
    for letter in n:
        #Here, if any letter is upper case we print _ left to it
        if letter.isupper():
            print("_" + letter.lower(), end="")
        else:
            print(letter,end="")
    print()

main()