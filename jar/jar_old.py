import emoji
cookie=emoji.emojize(':cookie:')


class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity


    def __str__(self):
        cookie=emoji.emojize(':cookie:')
        return print(cookie*Jar.size)

    def deposit(self, n):
        cookieTotal=+n

    def withdraw(self, n):
        cookieTotal=-n

    def cookieTotal(self,n):
        self.cookieTotal=cookieTotal

    @property
    def capacity(self):
        pass

    @property
    def size(self):
        self.size=self


