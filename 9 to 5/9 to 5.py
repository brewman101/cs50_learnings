import re
import sys

# Capture hours
input="10:00 AM to 10:00 PM"
#input("Hours: ")

# Check that it meets correct formatting
# XX:XX AM to XX:XX PM
times=(re.search(r"([0-9]+):([0-9]+) ([A|P][M]) to ([0-9]+):([0-9]+) ([A|P][M])",input))
if times:

    if times.group(2)>59:
        raise ValueError
    if times.group(5)>59:
        raise ValueError
    
    

else:
    raise ValueError



# Split into two strings
# a,b=string1.split(" to ")
