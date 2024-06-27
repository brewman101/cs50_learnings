# import random
# from pyfiglet import Figlet
# figlet = Figlet()
# font=(figlet.getFonts())


# Figlet puzzle: https://cs50.harvard.edu/python/2022/psets/4/figlet/
# Completed


import sys
from pyfiglet import Figlet
figlet = Figlet()
import random
font_choice=(sys.argv[2])
font_list=figlet.getFonts()

if (len(sys.argv)<3):
    sys.exit("Invalid usage")

if (sys.argv[1]) != "-f":
    sys.exit("Invalid usage")

if font_choice not in font_list:
    sys.exit("Invalid usage")

capture=input("Input: ")
figlet = Figlet()
#random_choice=random.randint(0,549)
figlet.setFont(font=font_choice)
print(figlet.renderText(capture))



