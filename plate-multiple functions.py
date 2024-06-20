

def main():
    plate="12RC"
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
    else:
        return True

# Check the length
def check_length(plate):
    if len(plate) < 7:
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

main()

#check_firstTwo("19hnd")
