import sys
import os

count=0
if len(sys.argv) != 2:
    sys.exit("Zero command line arguments")
script=sys.argv[1]
if script[-3:] != ".py":
    sys.exit("Not a python script")

try:
    open(sys.argv[1], "r")
except FileNotFoundError:
    sys.exit("File not found")
with open(sys.argv[1]) as file:
    for line in file:
        if line[0]==" ":
            line=line.lstrip()
        if line.isspace():
            pass
        elif line[0]=="#":
            pass
        else:
            count=count+1

print(count)
# Insert code here to read all lines, excluding any that start with # or are blank
