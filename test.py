import sys
import emoji
cookie=emoji.emojize(':cookie:')



class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            sys.exit(ValueError)
        self.capacity=capacity
        self.size=0

    def __str__(self):
        return f"{self.size * cookie}"
    
    def deposit(self, n):
        if n + self.size > self.capacity:
            sys.exit(ValueError)
        self.size=self.size + n
      
    def withdraw(self, n):
        if n - self.size < 0:
            sys.exit(ValueError)
        self.size=self.size-n

"""
    @property
    def capacity(self):
        pass

    @property
    def size(self):
        pass
"""

jar=Jar()
jar.deposit(4)
jar.withdraw(1)
print(jar)