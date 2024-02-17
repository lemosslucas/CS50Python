# Import the fuctions in bank.py
import bank

def main():
    # Call all the fuctions
    test_0()
    test_20()
    test_100()

def test_0():
    # Test if the program return 0
    assert bank.value("hello, newman") == 0
    assert bank.value("Hello") == 0

def test_20():
    # Test if the program return 20
    assert bank.value("hey") == 20
    assert bank.value("hi") == 20

def test_100():
    # Test if the program return 100
    assert bank.value("what's happening?") == 100
    assert bank.value("what's up?") == 100

if __name__ == "__main__":
    main()
