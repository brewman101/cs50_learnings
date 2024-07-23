import response

def test1():
    assert response.validate("test@test.com")=="Valid"

def test2():
    assert response.validate("test@@@test.com")=="Invalid"
