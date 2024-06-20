import string
exlcusions=string.punctuation + " "

def main():
    plate="RC12"
    # plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #print(s)
    if check_length(s) is False:
        return False
    elif check_firstTwo(s) is False:
        return False
    elif punctuation(s) is False:
        return False    
    else:
        return True

# Check the length is between 2 and 6 characters
def check_length(plate):
    if len(plate) < 7 and len(plate) >1:
        return True
    else:
        return False

# Check the first two characters are letters
def check_firstTwo(plate):
    # check for valid
    if (plate[0:2]).isalpha() is True:
        return True
    else:
        return False

# Check for periods, spaces or punctuation
def punctuation(p):
    if any(char in exlcusions for char in p):
        return False
    else:
        return True


main()

#check_firstTwo("19hnd")
