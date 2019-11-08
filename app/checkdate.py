# year = int(input("Year: "))
# month = int(input("Month: "))
# day = int(input("Day: "))


def month_day_check(year, month, day):
    if (1 <= month <= 12) and (isinstance(month, int)):
        if month % 2 == 1 or month == 8:    # Odd months and August have 31 days
            if 1 <= day <= 31:
                return True
            else:
                return False
        elif month == 2 and year % 4 == 0:  # Febuary during Leap years have 29 days
            if 1 <= day <= 29:
                return True
            else:
                return False
        elif month == 2:                    # Feburary has 28 days
            if 1 <= day <= 28:
                return True
            else:
                return False
        else:
            if 1 <= day <= 30:              # Even months excluding August have 30 days
                return True
            else:
                return False
    else:
        return False

# print(month_day_check(month, day))


if __name__ == '__main__':
    print(month_day_check(2019, 11, 400))
