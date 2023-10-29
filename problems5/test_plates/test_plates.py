from plates import is_valid

def test_empty():
    assert is_valid("") == False

def test_starts_with_2_letters():
    assert is_valid("AB") == True
    assert is_valid("1A") == False
    assert is_valid("A1") == False

def test_length():
    assert is_valid("CD") == True
    assert is_valid("TOOMANY") == False
    assert is_valid("A") == False

def test_numbers():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False
    assert is_valid("AAA222") == True

def test_punctuations():
    assert is_valid("AAA.12") == False
    assert is_valid("AAA BC") == False
    assert is_valid("AA.,!?") == False
