import sys,os
from PIL import Image, ImageOps

# In main function we measure the length of our sys arguments
def main():
    length = len(sys.argv)
    if length > 3:
        sys.exit("Too many command-line arguments")
    elif length < 3:
        sys.exit("Too few command-line arguments")
    # When we have the rigth length of arguments (3), we define each one with a variable
    else:
        first = sys.argv[1]
        second = sys.argv[2]
        # Variables transfer to file_check function
        file_check(first,second)

def file_check(first,second):
    # Using OS module, we split and get the image format
    a = os.path.splitext(first)
    b = os.path.splitext(second)
    # Here we compare image formats for our arguments
    if a[1] == b[1]:
        file_open(first,second)
    else:
        sys.exit("Input and output have different extensions")


def file_open(first,second):
    # In this function we open up shirt as a shirt.png image to get the size of it and later overlay it on the other image
    try:
        shirt = Image.open("shirt.png",mode= "r")
        size = shirt.size
    # We open our first inputted argument as a file
        forfit = Image.open(first,mode="r")
    # cropping and fitting it for the size of our shirt.png
        forfit = ImageOps.fit(forfit,size)
    # Pasting shirt.png on our cropped image and later saving it
        forfit.paste(shirt,shirt)
        forfit.save(second)
# Expecting that our file may not exist
    except FileNotFoundError:
        sys.exit("Invalid input")



main()
