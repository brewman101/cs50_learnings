# Program for https://cs50.harvard.edu/python/2022/psets/4/adieu/
# Solution completed

import sys
names_format=""
names=[]
while True:
    try:
       in_name=input("Name: ")
       names.append(in_name)
    except (KeyError, EOFError) :
        break
total=len(names)
total=total-1
total=range(total)
if len(names)==1:
    print(f"Adieu, adieu, to {names[0]}")
elif len(names)==2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")
elif len(names)>2:
    for _ in total:
        names_format=names_format+(names[_])+", "
    print(f"Adieu, adieu, to {names_format}and {names[-1]}")
