#Now, we are asking our user a qustion and storing it in a variable below, called 'x'
x = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

#We should remember that 42 is inputed as a string in a x variable, so we need brackets
if x.strip() == "42":
    print("Yes")
#We should convert information in x into lower-case letters with no spaces in between
elif x.lower().strip() == "forty-two":
    print("Yes")
elif x.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")