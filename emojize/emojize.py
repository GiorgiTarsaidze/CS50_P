import emoji
#Ask for input value and send it to the other function
def main():
    inputed = input("Input: ")
    emojized(inputed)
#Print the output using library method
def emojized(emo):
     print("Output: " + emoji.emojize(emo))
#Summon the function
main()


# user_input = input("Input: ")
# output = emoji.emojize(user_input, language = 'alias')
# print(f"Output: {output}")