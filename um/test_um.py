import um
import pytest

def test1():
    assert um.count("um")==1

def test2():
    assert um.count(" um ")==1

def test3():
    assert um.count("Um")==1

def test4():
    assert um.count("My mum said um")==1
