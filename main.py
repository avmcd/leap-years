
def is_leap(year):
    leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    return leap


def run_tests():
    test_values = [1996, 2000, 2004]
    # these should return no error msg
    for _ in test_values:
        assert is_leap(_) == True, 'should be True'

if __name__ == '__main__':
    run_tests()

    year = int(input())
    print(is_leap(year))
