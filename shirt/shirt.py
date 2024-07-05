# import modules

import sys
from PIL import Image

# Too few command-line arguments
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")


# Too many command-line arguments
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")

file1=sys.argv[1]
file2=sys.argv[2]

if file1[-3:] != file2[-3:]:
    sys.exit("Input and output have different extensions")
