input1 = input("Input: ").strip()
print("Output: ", end="")

for letter in input1:
    #Remove all the vowels both in upper-case and lower-case and continue iteration without them
    if letter in ['a','A','e','E','i','I','o','O','u','U']:
        continue
    else:
        print(letter,end="")
#New line
print()


