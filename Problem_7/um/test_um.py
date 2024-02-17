import um

def main():
    test_cases()
    test_word_um()
    test_spaces()

def test_cases():
    assert um.count("Um, thanks for the album") == 1
    assert um.count("Um, thanks, um...") == 2

def test_word_um():
    assert um.count("yummy") == 0

def test_spaces():
    assert um.count("Hello um world") == 1
    assert um.count("um?") == 1

if __name__ == "__main__":
    main()
