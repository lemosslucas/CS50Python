# Import the fuctions of fuel.py
import fuel
# import the fuctions of pytest for help to do a exception
import pytest

def main():
    # Call the fuctions
    test_input()
    test_Error()
# Check the error
def test_Error():
    # If has a raizes == exception, the program it was correct
    with pytest.raises(ZeroDivisionError):
        fuel.convert("25/0")
        fuel.convert("75/0")
        fuel.convert("100/0")
    with pytest.raises(ValueError):
        fuel.convert("dog/cat")
        fuel.convert("four/five")
# Test if the inputs are corrects
def test_input():
    assert fuel.convert("1/4") == 25 and fuel.gauge(25) == "25%"
    assert fuel.convert("1/100") == 1 and fuel.gauge(1) == "E"
    assert fuel.convert("99/100") == 99 and fuel.gauge(99) == "F"
    assert fuel.convert("3/4") == 75 and fuel.gauge(75) == "75%"

if __name__ == "__main__":
    main()
