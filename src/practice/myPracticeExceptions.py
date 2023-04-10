""" My Practice - Scratch Lab """


def leap_year_demo(year: int):
    try:
        greeting = input('This will check if a year is a leap year.\nNow press Enter key.')
        year = int(input('Please input year in question.'))
    except OverflowError:
        print('You have entered too many digits; year must contain only four digits.')
    else:
        if year % 400 == 0 and year % 100 == 0:
            print(f'Your {year} is a leap year.')
        elif year % 4 == 0 and year % 100 != 0:
            print(f'Your {year}, is a leap year.')
        else:
            print(f'Your {year}, is not a leap year.')


if __name__ == '__main__':
    leap_year_demo(123)

