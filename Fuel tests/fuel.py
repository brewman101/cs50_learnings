import sys

def main():
    fuel=gauge(input("Fraction "))
    print(fuel)

def convert(fraction):
    try:
        a,b=fraction.split("/")
        a=int(a)
        b=int(b)
        if a>b:
            pass
        else:
            fraction=(a/b)*100
            fraction=round(fraction)
    except ValueError:
        sys.exit("Value Error")
    if fraction==0 or fraction==1:
        return("E")
    elif fraction==100 or fraction==99:
        return("F")
    else:
        fraction=(f"{int(fraction)}%")
        return(fraction)


def gauge(percentage):
    response=convert(percentage)
    return(response)






if __name__ =="__main__":
    main()
