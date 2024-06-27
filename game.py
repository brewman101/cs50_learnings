# Problem https://cs50.harvard.edu/python/2022/psets/4/game/


guess=0
import random

level=0
while level < 1:
    try:
        level=int(input("Level: "))
    except (ValueError, EOFError):
        continue
result=(random.randrange(1,level))

while guess != result:
    try:
        guess=int(input("Guess: "))
        if guess > result:
            print("Too large!")
        elif guess < result:
            print("Too small!")
    except (ValueError, EOFError):
        continue
print("Just Right!")
