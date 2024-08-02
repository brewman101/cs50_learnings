import sys
import emoji
cookie=emoji.emojize(':cookie:')



class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            sys.exit(ValueError)
        self._capacity=capacity
        self._size=0

    def __str__(self):
        return f"{self.size * cookie}"
    
    def deposit(self, n):
        if n + self.size > self.capacity:
            sys.exit(ValueError)
        self._size=self.size + n
      
    def withdraw(self, n):
        if self._size - n < 0:
            sys.exit(ValueError)
        self._size=self.size-n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


jar=Jar()
jar.deposit(1)
print(jar)