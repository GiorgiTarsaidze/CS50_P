# x is an integer
# y is +, -, *, or /
# z is an integer

a = input("Expression: ").strip()
#We remove the spacebars in between and then we split our expression in three different variables
x,y,z = a.split(" ")

#Convert our variables into floats
x = float(x)
z = float(z)

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
# here we asuume that y can't have any other meanings then +,-,*,/ . That's why we put "else" in there
else:
    print(x / z)

