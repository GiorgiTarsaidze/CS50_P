import requests
import sys


try:
# if length of our command-line argument is 2 and is float then we can work with it
    if len(sys.argv) == 2 and type(float):
        # a variable stores our bitcoin exchange index with a float type
        a = float(sys.argv[1])
        # using requests lib we get information
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoin = r.json()
        # price variable stores float information and searchs in r dictionarty which we requested for desired value
        # Also we replace "," so that it can be readable in float type
        price = float(bitcoin["bpi"]["USD"]["rate"].replace(",",""))

        result = price*a
        result = f"${result:,.4f}"


        print(result)
    else:
        sys.exit("Missing command-line argument")

except ValueError:
    sys.exit("Missing command-line argument")

except requests.RequestException:
    sys.exit("Missing command-line argument")