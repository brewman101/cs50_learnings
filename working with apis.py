# Problem from here:  https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
import requests
import sys
import json

# Get a request from the api
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
# load the text portion to a variable
output=json.loads(r.text)
# output the json response in a tidy format
print(json.dumps(output, indent=2))



