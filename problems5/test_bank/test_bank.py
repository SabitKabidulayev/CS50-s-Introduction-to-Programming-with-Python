from bank import value

def test_default():
    assert value("") == 100

def test_hello():
    assert value("hello") == 0
    assert value("hello, customer") == 0
    assert value("HElLo, customer") == 0

def test_h():
    assert value("h") == 20
    assert value("He") == 20
    assert value("house") == 20

def test_other():
    assert value("random string") == 100
    assert value("12345,.?") == 100