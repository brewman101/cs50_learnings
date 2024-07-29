import emoji
cookie=emoji.emojize(':cookie:')


class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity


    def __str__(self):
        return f"{cookie}"

    def deposit(self, n):
        cookieTotal=+n

    def withdraw(self, n):
        cookieTotal=-n

    @property
    def capacity(self):
        pass

    @property
    def size(self):
        pass

