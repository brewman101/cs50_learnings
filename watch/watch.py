import re
import sys

url=input("URL: ").strip()

matches=re.search(r'^https?://(www.\.)?youtube\.com/embed/(.+$)',url, re.IGNORECASE)
if matches:
    print(f"Username: ", matches.group(2))































# def main():
#     print(parse(input("HTML: ")))


# def parse(s):
#     s=re.search(r'(?<=https://)\w+',s)
#     s=s.group(0)  
#     return s




# if __name__ == "__main__":
#     main()