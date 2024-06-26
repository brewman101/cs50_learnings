# import random
# from pyfiglet import Figlet
# figlet = Figlet()
# font=(figlet.getFonts())


# Figlet puzzle: https://cs50.harvard.edu/python/2022/psets/4/figlet/
# What I have so far

from pyfiglet import Figlet
import random
capture=input("Input: ")
figlet = Figlet()
random_choice=random.randint(0,549)
#print(figlet.renderText("string"))
my_list=(figlet.getFonts())
choice=my_list[random_choice]
figlet.setFont(font=choice)
print(figlet.renderText(capture))

