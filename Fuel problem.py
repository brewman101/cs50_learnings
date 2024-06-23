# Prompt for fuel input


def main():
    while True:
        fuel=input("Fraction: ")
        try:
            a,b=fuel.split("/")
            a=int(a)
            b=int(b)
            if a>b:
                continue
            else:
                fuel=(a/b)*100
                fuel=round(fuel)
        except ValueError:
            pass
            continue
        if fuel==0 or fuel==1:
            print("E")
            break
        elif fuel==100 or fuel==99:
            print("F")
            break
        else:
            print(f"{int(fuel)}%")
            break


main()
