from Lecture5 import square

def main():
    test_Lecture5()

def test_Lecture5():
    # One way I can test my code
    # if square(2) !=4:
    #     print("2 squared was not 4")
    # if square(3) !=9:
    #     print("3 squared was not 9")
    # else:
    #     print("Program working fine")
    
    # alternatively I can use the assert function
    try:
        assert square(2)==4
        assert square(4)==16
    except AssertionError:
        print("Program has problems")

if __name__ =="__main__":
    main()

assert square(3)==9