import seasons

def main():
    test_calculed_minutes()

def test_calculed_minutes():
    assert seasons.minutes_quant("2023-02-08") == "Five hundred twenty-five thousand, six hundred minutes"
    assert seasons.minutes_quant("2022-02-08") == "One million, fifty-one thousand, two hundred minutes"
    assert seasons.minutes_quant("2023 December, 14") == ValueError

if __name__ == "__main__" :
    main()
