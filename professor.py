# Coding problem https://cs50.harvard.edu/python/2022/psets/4/professor/ 

import random



def main():
    level=get_level()
    points=0
    for _ in range(10):
        number1=generate_integer(level)
        number2=generate_integer(level)
        result=number1+number2
        result_attempt=0
        attempt=0
        while attempt!=3:
            result_attempt=int(input(f"{number1} + {number2} = "))
            if result_attempt==result:
                points=points+1
                break
            elif result_attempt!=result:
                attempt=attempt+1
                print("EEE")
        print(f"{number1} + {number2} = {result}")


def get_level():

    while True:
        try:
            n = int(input("Level: "))
            if n > 0 and n < 4:
                break
        except ValueError:
            print("")
    return n




def generate_integer(level):
    if level==1:
        number1=random.randint(0,9)
        return number1
    elif level==2:
        number1=random.randint(10,99)
        return number1
    elif level==3:
        number1=random.randint(100,999)
        return number1

if __name__ == "__main__":
    main()
