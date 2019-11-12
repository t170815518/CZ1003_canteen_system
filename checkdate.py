#Function by Wee Li
def month_day_check(year, month, day):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if isinstance(day, int) and 1 <= day <= 31:
            return True
        else:
            return False
    elif month in [4, 6, 9, 11]:
        if isinstance(day, int) and 1 <= day <= 30:
            return True
        else:
            return False
    elif month == 2:
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            if isinstance(day, int) and 1 <= day <= 29:
                return True
            else:
                return False
        else:
            if isinstance(day, int) and 1 <= day <= 28:
                return True
            else:
                return False
    else:
        return False


if __name__ == '__main__':
    # year = int(input("Year: "))
    # month = int(input("Month: "))
    # day = int(input("Day: "))
    print(month_day_check(2019, 2, 29))
