#Importing random lib
import random as r
import sys

# in fucntion called main, we create a while loop
def main():
    while True:
        try:
            level = int(input("Level: ")) #if our inputted level is not positive integer, we repeat the loop
            if level > 0:
                guess(level)
                
            else:
                continue
        except ValueError: # expect that our inputted value is not int, repeat the loop
            continue
# Another function, with while loop, that get the value if our "level" variable is positive
def guess(n):
    while True:
        try:
            guess_num = int(input("Guess: "))
            if guess_num <=0:
                continue
            elif guess_num < r.randint(1,n): #checking if Guess number is in between random number between 1 and n
                print("Too small!")
            elif guess_num > r.randint(1,n):
                print("Too large!")
            else:
                sys.exit("Just right!")

        except ValueError:
            continue
main()