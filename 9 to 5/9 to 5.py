import re
import sys

# Capture hours
amount="5 AM to 10 PM"
#amount=input("Hours: ")

# Check that it meets correct formatting
# XX:XX AM to XX:XX PM
times=(re.search(r"([0-9]+)(:)?([0-9]+)? ([A|P][M]) to ([0-9]+)(:)?([0-9]+)? ([A|P][M])",amount))
if times and times.group(2)!=None:
    if int(times.group(3))>59:
        raise ValueError
    else:
        b=int(times.group(3))
    if int(times.group(7))>59:
        raise ValueError
    else:
        d=int(times.group(7))
    if times.group(4)=="PM":
        a=int(times.group(1))+12
    else:
        a=int(times.group(1))
    if times.group(8)=="PM":
        c=int(times.group(5))+12
    else:
        c=int(times.group(5))

elif times and times.group(2)==None:
    if times.group(4)=="PM":
        a=int(times.group(1))+12
    else:
        a=int(times.group(1))
    if times.group(8)=="PM":
        c=int(times.group(5))+12
    else:
        c=int(times.group(5))
    b=int(00)
    d=int(00)

else:
    raise ValueError


print(f"{a:02d}:{b:02d} to {c:02d}:{d:02d}")

