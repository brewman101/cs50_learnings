from datetime import date
from datetime import datetime
import sys
import re
import inflect
import math
p = inflect.engine()


def main():
    check=validate_date(input("Date of Birth: "))
    print(check)

def validate_date(v):
    today=date.today()
    r=re.search(r"\d\d\d\d-\d\d-\d\d",v)
    if r:
        v=datetime.strptime(v, '%Y-%m-%d').date()
        v=today-v
        v=int(v.total_seconds())/60
        v=math.floor(v)
        v=p.number_to_words(v, andword='')
        v=v.capitalize()
        v=(v + " minutes")
        return v
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
