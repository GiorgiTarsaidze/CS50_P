import csv, sys


#Empty list, where we will append our columns
before = []

# In the main function we measure the length of our sys arguments
def main():
    length = len(sys.argv)
    if length < 3:
        sys.exit("Too few command-line arguments")
    elif length > 3:
        sys.exit("Too many command-line arguments")
    else:
        a = sys.argv[1]
        b = sys.argv[2]
        if a.endswith(".csv") and b.endswith(".csv"):
            # sending our arguments to file_check function if all the criterias are good
            file_check(a,b)
        else:
            sys.exit("Not a CSV file")

def file_check(a,b):
    try:
        # opening an existing file with a DictReader
        with open(a) as file:
            reader = csv.DictReader(file)
        # For each row in our file, we append it to our empty list above
            for row in reader:
                before.append(row)
        # Re-writing our values to a new file
            with open(b, "w") as file:
                    writer = csv.DictWriter(file, fieldnames=["first","last","house"])
                    # Headlines as a first row
                    writer.writeheader()
                    for i in before:
                        #We split our name and surname to a list
                        last,first = i["name"].split(",")
                        #Here, we get rid of an empty spaces
                        first = first.replace(" ","")
                        #Getting the house column from the dictionary
                        house = i["house"]
                        #Writing each row in our new file
                        writer.writerow({'first':first,'last':last,'house':house})
# Expecting that our file might not exist
    except FileNotFoundError:
        sys.exit(f"Could not read {a}")

main()

