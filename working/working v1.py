import re
import sys

# Capture hours

def main():
    print(convert(input("Hours: ")))


# Check that it meets correct formatting
# XX:XX AM to XX:XX PM
def convert(s):
    s=(re.search(r"([0-9]+)(:)?([0-9]+)? ([A|P][M]) to ([0-9]+)(:)?([0-9]+)? ([A|P][M])",s))
    if s and s.group(2)!=None:
        a=int(s.group(1))
        c=int(s.group(5))
        if int(s.group(3))>59:
            raise ValueError
        else:
            b=int(s.group(3))
        if int(s.group(7))>59:
            raise ValueError
        else:
            d=int(s.group(7))
        if s.group(4)=="PM" and a!=12:
            a=int(s.group(1))+12
        else:
            a=int(s.group(1))
        if s.group(8)=="PM" and c!=12:
            c=int(s.group(5))+12
        else:
            c=int(s.group(5))
        if a==12 and s.group(4)=="AM":
            a=0
        elif c==12 and s.group(8)=="AM":
            a=0
    elif s and s.group(2)==None:
        a=int(s.group(1))
        c=int(s.group(5))
        if s.group(4)=="PM" and a!=12:
            a=int(s.group(1))+12
        else:
            a=int(s.group(1))
        if s.group(8)=="PM" and c!=12:
            c=int(s.group(5))+12
        else:
            c=int(s.group(5))
        if a==12 and s.group(4)=="AM":
            a=0
        elif c==12 and s.group(8)=="AM":
            a=0
        b=int(00)
        d=int(00)

    else:
        raise ValueError

    s=(f"{a:02d}:{b:02d} to {c:02d}:{d:02d}")
    return s

if __name__ == "__main__":
    main()
