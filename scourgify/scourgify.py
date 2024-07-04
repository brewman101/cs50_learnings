import sys
import csv
dictionary=dict()
# Too few command-line arguments
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")


# Too many command-line arguments
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")

argument1=sys.argv[1]
argument2=sys.argv[2]

# Verify input file
try:
    open(argument1, "r")
except FileNotFoundError:
    sys.exit(f"Could not read {argument1}")

with open(argument1, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        lastName,firstName=(row['name']).split(",")
        print(firstName,lastName, row['house'])
