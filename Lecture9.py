# balance=0

# def main():
#     print("Balance: ", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance: ", balance)


# def deposit(n):
#     global balance
#     balance+=n

# def withdraw(n):
#     global balance
#     balance-=n

# if __name__ =="__main__":
#     main()

#######################################################

class Account:
    def __init__(self):
        self._balance=0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance +=n
    
    def withdraw(self, n):
        self._balance-=n

def main():
    account=Account()
    print("Balance", account.balance)
    account.deposit(200)
    account.withdraw(75)
    print("Balance", account.balance)

if __name__ =="__main__":
    main()

#########################################################

class Cat:
    MEOWS=3
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat=Cat()
cat.meow()