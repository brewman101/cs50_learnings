# def Find(string):
#     x=string.split()
#     res=[]
#     for i in x:
#         if i.startswith("https://www.youtube.com"):
#             res.append(i)
#     return res
             
# # Driver Code
# string = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
# print("Urls: ", Find(string))

import re
import sys

# Capture hours
amount="5 AM to 10 PM"
#amount=input("Hours: ")

# Check that it meets correct formatting
# XX:XX AM to XX:XX PM
times=(re.search(r"([0-9]+)(:)?([0-9]+)? ([A|P][M]) to ([0-9]+)(:)?([0-9]+)? ([A|P][M])",amount))
print(times.group(8))