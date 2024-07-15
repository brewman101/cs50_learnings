import re
import sys

# Capture hours
input="10:00 AM to 10:00 PM"
#input("Hours: ")

# Check that it meets correct formatting
# XX:XX AM to XX:XX PM
print(re.search(r"[0-9]+:[0-9]+ AM to [0-9]+:[0-9]+ PM", input))


# Split into two strings
# a,b=string1.split(" to ")
