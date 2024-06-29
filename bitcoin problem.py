# Problem from here:  https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
import requests
import sys
import json
# Attempt to convert the argument to a float.
try:
    coin=float(sys.argv[1])
# Error if a string is provided
except ValueError:
    sys.exit("Command-line argument is not a number")

# Exit with error code if too few arguments are provided
if len(sys.argv)<2:
    sys.exit("Missing command-line argument")


while True:
    # Attempt to request
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        output=json.loads(r.text)
        bitcoin_price=(output['bpi']['USD']['rate'])
        bitcoin_price=bitcoin_price.replace(",","")
        bitcoin_price=float(bitcoin_price)
        break
    except requests.RequestException:
        print("Error")

# Print number of coins by the rate of bitcoin
total=coin*bitcoin_price
print(f"${total:,.4f}")
