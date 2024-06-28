
def main():
    number=get_number()
    woof(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def woof(n):
    for _ in range(n):
        print("woof")

main()