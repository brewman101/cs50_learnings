# For list using a list

# One option
for i in [0,1,2]:
    print("Woof")

# Better option
for i in range(3):
    print("Meow")

# Improvement replace i with _ so people can see it's unimportant in code
for _ in range(3):
    print("Meow")

# \n is the exit character.  Adding end="" this removes empty line
print("woof\n"*3, end="")