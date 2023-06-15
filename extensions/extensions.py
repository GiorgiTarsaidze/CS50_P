#Storing our input value in variable, called 'file' and removing all the spacebars in between
file = input("File name: ").lower().strip()
#According to common MIME types, we detected some of the types of our formats
#Using if/elif/else printing out proper answers to each type in our variable
if '.gif' in file:
    print("image/gif")
elif '.jpg' in file:
    print("image/jpeg")
elif '.jpeg' in file:
    print("image/jpeg")
elif '.png' in file:
    print("image/png")
elif '.pdf' in file:
    print("application/pdf")
elif '.txt' in file:
    print("text/plain")
elif '.zip' in file:
    print("application/zip")
else:
    print("application/octet-stream")