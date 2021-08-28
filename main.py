
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #run tests


    year = int(input())
    print(is_leap(year))
