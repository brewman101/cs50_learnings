import fuel

def test_case1():
    assert fuel.gauge("3/4")=="75%"

def test_case2():
    assert fuel.gauge("1/4")=="25%"


