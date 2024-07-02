import sys

if len(sys.argv) != 2:
    sys.exit("Zero command line arguments")
script=sys.argv[1]
if script[-3:] != ".py":
    sys.exit("Not a python script")
script=open(sys.argv[1], "r")
try:
    script.read()
except FileNotFoundError:
    sys.exit("File not found")


# Insert code here to read all lines, excluding any that start with # or are blank
