#The whole code in in a while True loop
#We split our fraction in two different variables
while True:
    try:
        x,y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
#Cases where x shouldnt be greater than y and where y shouldnt be 0. Here we continue our iteration
        if x>y:
            continue
        elif y==0:
            continue
#Exception of value error. For instance, if x or y is not int
    except ValueError:
        continue
    else:
        try:
#We store x/y into result, round it to a whole number and multiply by 100 to turn it into percentage
            result = round(x/y*100)
#Here we expect that y might be 0 and continue iterating on this case
        except ZeroDivisionError:
            continue
        except ValueError:
            continue
#Our result value is in percantages, so here, using "if" we write the code for E and F cases
        else:
            if result <= 1:
                print("E")
                break
            elif result >= 99:
                print("F")
                break
            else:
#We convert our result integer value into string and add % mark at the end
                result = str(result)
                print(result+"%", end="")
                break
