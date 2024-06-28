# Rock paper scissors
import random
resume=""

options={
    1:"Rock",
    2:"Paper",
    3:"Scissors"
}

while True:
    opponent_choice=(random.randint(1,3))
    print("")
    print("")
    print("Choose an Option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    choice=int(input("Choice: "))
    if choice==4:
        break
    elif choice==1:
        print(f"Your opponent chose {options[opponent_choice]}")
        if choice==opponent_choice:
            print("It's a tie!")
        elif opponent_choice==2:
            print("Paper beats Rock, you lose!  :( ")
        elif opponent_choice==3:
            print("Rock beats Scissors, you win!")
    elif choice==2:
        print(f"Your opponent chose {options[opponent_choice]}")
        if choice==opponent_choice:
            print("It's a tie!")
        elif opponent_choice==3:
            print("Scissors beats Paper, you lose!  :( ")
        elif opponent_choice==1:
            print("Paper beats Rock, you win!")
    elif choice==3:
        print(f"Your opponent chose {options[opponent_choice]}")
        if choice==opponent_choice:
            print("It's a tie!")
        elif opponent_choice==1:
            print("Paper beats Rock, you win!  :) ")
        elif opponent_choice==2:
            print("Scissors beats Paper, you lose!")
    resume=input("")
print("Thanks for playing")