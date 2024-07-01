import twttr

def test_twitter1():
    assert twttr.shorten("Test")=="Tst"
def test_twitter2():
    assert twttr.shorten("guild")=="gld"
def test_twitter3():
    assert twttr.shorten("hellO.world")=="hll.wrld"
def test_twitter4():
    assert twttr.shorten("Twitter")=="Twttr"
def test_twitter5():
    assert twttr.shorten("1234")=="1234"


