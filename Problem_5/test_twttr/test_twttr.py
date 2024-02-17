#Import the fuctions of twttr.py
import twttr

def main():
    # Called the fuctions
    test_cases()
    test_numbers()
    test_ponctuation()

def test_cases():
    # Verify if the module was called correct
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("TWITTER") == "TWTTR"
    assert twttr.shorten("TwItTeR") == "TwtTR"
def test_numbers():
    # Verify if the module was called correct
    assert twttr.shorten("1234") == "1234"
def test_ponctuation():
    # Verify if the module was called correct
    assert twttr.shorten("!?.,") == "!?.,"
    
if __name__ == "__main__":
    main()