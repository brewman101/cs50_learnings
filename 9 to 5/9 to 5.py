import re
import sys

# Capture hours
#input="10:00 AM to 10:00 PM"
amount=input("Hours: ")

# Check that it meets correct formatting
# XX:XX AM to XX:XX PM
times=(re.search(r"([0-9]+):([0-9]+) ([A|P][M]) to ([0-9]+):([0-9]+) ([A|P][M])",amount))
if times:

    if int(times.group(2))>59:
        raise ValueError
    if int(times.group(5))>59:
        raise ValueError
    if times.group(3)=="PM":
        a=int(times.group(1))+12
    else:
        a=int(times.group(1))
    if times.group(6)=="PM":
        c=int(times.group(4))+12
    else:
        c=int(times.group(4))


else:
    raise ValueError


print(f"{a:02d}:{times.group(2)} to {c:02d}:{times.group(5)}")

