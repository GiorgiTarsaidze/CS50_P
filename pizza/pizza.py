import sys
import csv
from tabulate import tabulate

# In the main function we check for the argument length
def main():
    m = len(sys.argv)

    if m < 2 :
        sys.exit("Too few command-line arguments")
    elif m > 2:
        sys.exit("Too many command-line arguments")
    else:
# If our argv length that is inside m variable is 2, we pass the second argument to converter function
        name = sys.argv[1]
        print(converter(name))

def converter(name):
    if name.endswith(".csv"):
        try:
# Creating an empty list to append our csv rows
            menu_list = []
# Opening our csv file and reading using csv reader method
            with open(name) as file:
                reader = csv.reader(file)
# Going for each row in the reader and appending to an empty list
                for row in reader:
                    menu_list.append(row)
# Thus, first list in the row is our header list and anything after is the menu
            headers = menu_list[0]
            menu = menu_list[1:]
# Using tabulate module syntax, creating an ASCII art table 
            return tabulate(menu,headers, tablefmt="grid")



        except FileNotFoundError:
            sys.exit("File does not exist")

    else:
        sys.exit("Not a CSV file")

main()