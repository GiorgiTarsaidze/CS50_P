from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

# This list stores two exception cases
x = ['-f', '--font']

# This is the case where there is not argv argument, just the input
if len(sys.argv) == 1:
    # get random font wwhen there is no argument
    figlet.setFont(font = random.choice(figlet.getFonts()))
    #\n to start on next line
    print("Output: ", figlet.renderText(input("Input: ")), sep = "\n")

# This is the case where there is a command argument along with string input
elif len(sys.argv) == 3 and sys.argv[1] in x and sys.argv[2] in figlet.getFonts():
    figlet.setFont(font = sys.argv[2])
    print("Output: ", figlet.renderText(input("Input: ")), sep = "\n")
else:
    sys.exit("Invalid usage")
