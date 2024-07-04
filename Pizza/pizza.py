# Solution to https://cs50.harvard.edu/python/2022/psets/6/pizza/

import sys
from tabulate import tabulate
import csv



# Check if it has too few arguments
if len(sys.argv) <2:
    sys.exit("Too few command-line arguments")
# Check if it has too many arguments
if len(sys.argv) >2:
    sys.exit("Too many command-line arguments")

# Check the file exists
csvFile=sys.argv[1]
if csvFile.endswith(".csv") == False:
    sys.exit("Not a CSV file")

try:
    open(csvFile, "r")
except FileNotFoundError:
    sys.exit("File does not exist")

file = open(csvFile, "r")
data = list(csv.reader(file, delimiter=","))
file.close()
print(tabulate(data[1:],data[0],tablefmt="grid"))
