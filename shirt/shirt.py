# import modules
file2="shirt.png"
import os,sys
from PIL import Image, ImageOps
# Too few command-line arguments
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")

# Too many command-line arguments
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
if (sys.argv[1])[-3:] != (sys.argv[2])[-3:]:
    sys.exit("Input and output have different extensions")


try:
    image1=Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File doesn't exist")
shirt=Image.open(file2)
shirt_size=shirt.size
image1=ImageOps.fit(image1, shirt_size)
#image1.save(sys.argv[2])
image1.paste(shirt, shirt)
image1.save(sys.argv[2])
