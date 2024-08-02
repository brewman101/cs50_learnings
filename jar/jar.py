import sys
import emoji
cookie=emoji.emojize(':cookie:')



class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise ValueError ("Capacity cannot be negative")
        self._capacity=capacity
        self._size=0


    def __str__(self):
        return f"{self.size * cookie}"

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("Deposit exceeds capacity")
        self._size=self.size + n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("You have removed too many cookies")
        self._size=self.size-n


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    @property
    def size(self):
        return self._size

