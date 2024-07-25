from datetime import date
from datetime import datetime
import sys
import re



def main():
    check=validate_date(input("Date of Birth: "))
    print(check)

def validate_date(v):
    today=date.today()
    r=re.search(r"\d\d\d\d-\d\d-\d\d",v)
    if r:
        v=datetime.strptime(v, '%Y-%m-%d').date()
        v=today-v
        return v
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
