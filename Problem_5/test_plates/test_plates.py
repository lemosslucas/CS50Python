# Import the fuction of plates.py
import plates

def main():
    # Call all the test fuctions
    test_min_max()
    test_numbers_mid()
    test_start_two_letters()
    test_first_not_0()
    test_no_periods()
# Test the min and max of char in a plate
def test_min_max():
    assert plates.is_valid("AB") == True
    assert plates.is_valid("ABC456") == True
    assert plates.is_valid("A") == False
    assert plates.is_valid("ABCD234") == False
# Test if has number in mid
def test_numbers_mid():
    assert plates.is_valid("CS50P2") == False
    assert plates.is_valid("AACD22") == True
# Test if start two letters
def test_start_two_letters():
    assert plates.is_valid("AB") == True
    assert plates.is_valid("A4") == False
    assert plates.is_valid("4A") == False
# Test if not first a 0
def test_first_not_0():
    assert plates.is_valid("ABCD") == True
    assert plates.is_valid("ABC0") == False
# Test if has no periods in the plate
def test_no_periods():
    assert plates.is_valid("A CD") == False
    assert plates.is_valid("A?.4") == False

if __name__ == "__main__":
    main()
