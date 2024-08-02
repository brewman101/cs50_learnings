from jar import Jar


def test1():
    jar=Jar()
    assert str(jar)==""
def test2():
    jar=Jar()
    jar.deposit(1)
    assert str(jar)=="🍪"
def test3():
    jar=Jar()
    jar.deposit(3)
    assert str(jar)=="🍪🍪🍪"
def test4():
    jar=Jar()
    jar.capacity = 10
    assert str(jar)==""
