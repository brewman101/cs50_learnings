import re
import sys

# Capture hours

def main():
    print(convert(input("Hours: ")))


# Check that it meets correct formatting
# XX:XX AM to XX:XX PM
def convert(s):
    s=(re.search(r"([0-9]+)(:)?([0-9]+)? ([A|P][M]) to ([0-9]+)(:)?([0-9]+)? ([A|P][M])",s))
    #  Groups      ---1-----2-----3-----  ----4---     ----5----6----7----------8------
    if s:
        if s.group(3)==None:
            c=0
        else:
            c=int(s.group(3))
        if s.group(7)==None:
            g=0
        else:
            g=int(s.group(7))
        if c > 59 or 7>59:
            raise ValueError
        a=int(s.group(1))
        b=s.group(2)
        d=s.group(4)
        e=int(s.group(5))
        f=s.group(6)
        h=s.group(8)
        if d=="PM" and a!=12:
            a=a+12
        if h=="PM" and e!=12:
            e=e+12
        s=(f"{a:02d}:{c:02d} to {e:02d}:{g:02d}")
        return s
    else:
        raise ValueError


    
    # if s and s.group(2)!=None:
    #     a=int(s.group(1))
    #     c=int(s.group(5))
    #     if int(s.group(3))>59:
    #         raise ValueError
    #     else:
    #         b=int(s.group(3))
    #     if int(s.group(7))>59:
    #         raise ValueError
    #     else:
    #         d=int(s.group(7))
    #     if s.group(4)=="PM" and a!=12:
    #         a=int(s.group(1))+12
    #     else:
    #         a=int(s.group(1))
    #     if s.group(8)=="PM" and c!=12:
    #         c=int(s.group(5))+12
    #     else:
    #         c=int(s.group(5))
    #     if a==12 and s.group(4)=="AM":
    #         a=0
    #     elif c==12 and s.group(8)=="AM":
    #         a=0
    # elif s and s.group(2)==None:
    #     a=int(s.group(1))
    #     c=int(s.group(5))
    #     if s.group(4)=="PM" and a!=12:
    #         a=int(s.group(1))+12
    #     else:
    #         a=int(s.group(1))
    #     if s.group(8)=="PM" and c!=12:
    #         c=int(s.group(5))+12
    #     else:
    #         c=int(s.group(5))
    #     if a==12 and s.group(4)=="AM":
    #         a=0
    #     elif c==12 and s.group(8)=="AM":
    #         a=0
    #     b=int(00)
    #     d=int(00)

    # else:
    #     raise ValueError

    # s=(f"{a:02d}:{b:02d} to {c:02d}:{d:02d}")
    # return s

if __name__ == "__main__":
    main()

