# Solution to https://cs50.harvard.edu/python/2022/psets/6/pizza/

import sys
from tabulate import tabulate

# Check if it has too few arguments
if sys.argv <2:
    sys.exit("Too few command-line arguments")
# Check if it has too many arguments
if sys.argv >2:
    sys.exit("Too many command-line arguments")

# Check the file exists
csv=sys.argv[1]
try:
    open(csv, "r")
except FileNotFoundError:
    sys.exit("File does not exist")

