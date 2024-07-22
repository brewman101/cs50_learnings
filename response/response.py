import validators 

def main():
    x=validate(input("Enter an email address? "))
    print(x)

def validate(v):
    x=validators.email(v)
    if x==True:
        x="Valid"
        return x
    else:
        x="Invalid"
        return x



if __name__ == "__main__":
    main()