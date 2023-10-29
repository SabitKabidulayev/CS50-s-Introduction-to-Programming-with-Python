from twttr import shorten

def test_default():
    assert shorten("") == ""

def test_lowercase():
    assert shorten("twitter apple hello") == "twttr ppl hll"

def test_uppercase():
    assert shorten("twIttEr ApplE hEllO") == "twttr ppl hll"

def test_numbers():
    assert shorten("tw1tt3r 1234567890") == "tw1tt3r 1234567890"

def test_punctuation():
    assert shorten("tw.tt/r .,?!") == "tw.tt/r .,?!"