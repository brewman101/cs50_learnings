# names=[]

# for _ in range(3):
#     name=input("What's your name? ")
#     names.append(name)

# for name in sorted(names):
#     print(f"hello, {name}")
########################################

# name = input("What's your name? ")

# file=open("names.txt", "a")
# file.write(f"{name} \n")
# file.close


# name = input("What's your name? ")

# # this bit automatically closes the file
# with open("names.txt", "a") as file:
#     file.write(f"{name} \n")


with open("names.txt", "r") as file:
    lines=file.readlines()

for _ in lines:
    print(_.rstrip("\n"))
