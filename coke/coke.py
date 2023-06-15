#store the coke price, which is 50 in variable
coke_price = 50
#We create a loop so we cant reach the negative number of our coke price. and make it > 0
while coke_price > 0 :
    print("Amount Due:", coke_price)
    #We store the input value of customer's inserted coin in coin variable
    coin = int(input("Insert Coin:"))

    if coin == 25:
    #Every time the coin is 25/10/5 we subtract and update our 'coke_price' variable
        coke_price-=coin
    elif coin == 10:
        coke_price-=coin
    elif coin == 5:
        coke_price-=coin
    else:
        continue
#The thing that can happen, is that after we insert 25 cent coin, then 10 cent coin and again 25, it give negative number and for that reason we calculate the absolute value of our price
#So that we can calculate that negative number as a change
change = abs(coke_price)

print("Change Owed:", change)