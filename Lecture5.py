# calculator app

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

# main won't run by default unless it is specified
if __name__ == "__main__":
    main()