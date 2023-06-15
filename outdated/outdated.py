tveebi = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#All the code is in a while loop
while True:
# We store our user's input in date variable
    date = input("Date: ").strip().title()
#If our input format is MM/DD/YYYY then we follow code below:
    if "/" in date:
        try:
            # m - months, d - days, y - years
            m,d,y = date.split("/")
            m = int(m)
            d = int(d)
        except ValueError:
            pass
        else:
            #We dont want our months and days to be negative number or beyond 31 in case of days and beyond 12 in case of months
            if (1 <= m <= 12) and (1<= d <= 31):
                #We use  0:2 to format leading zeros in case of months or days
                print(f"{y}-{m:02}-{d:02}")
                break
# Here is the case when our user's input format is "MONTH DAY, YEAR" in letters
    elif "," in date:
        m,d,y = date.split()
        try:
            d = int(d.replace(",",""))
        except ValueError:
            pass
        else:
            if (1<=d <= 31):
                # we create for loop and measure length of our list
                for i in range(len(tveebi)):
                    if m == tveebi[i]:
                        #We add +1 because 0's number is January
                        m = f"{(i+1):02}"
                        print(f"{y}-{m}-{d:02}")
                break