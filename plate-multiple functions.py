import string
exlcusions=string.punctuation + " "

def main():
    plate = input("Plate: ")
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
    elif no_zero(s) is False:
        return False
    elif no_num_letter(s) is False:
        return False
    else:
        return True

# Check the length is between 2 and 6 characters
def check_length(c):
    if len(c) < 7 and len(c) >1:
        return True
    else:
        return False

# Check the first two characters are letters
def check_firstTwo(two):
    # check for valid
    if (two[0:2]).isalpha() is True:
        return True
    else:
        return False

# Check for periods, spaces or punctuation
def punctuation(p):
    if any(char in exlcusions for char in p):
        return False
    else:
        return True

# First number can't be 0
def no_zero(r):
    # Loop to find first number
    for _ in range(len(r)):
        # If first number is 0 return False (aka invalid)
        if (r[_]).isnumeric() is True and r[_]=="0":
            return False
        # If first number is 0 return True (aka valid)
        elif (r[_]).isnumeric() is True and r[_]!="0":
            return True
            
# No number then letter at the end
def no_num_letter(z):
    if (z[-2]).isalpha() is True and (z[-1]).isnumeric() is True:
        return False
    else:
        return True

main()
