import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s=s.lower()
    s=re.findall(r"\bum\b",s)
    s=len(s)
    return(s)





if __name__ == "__main__":
    main()
