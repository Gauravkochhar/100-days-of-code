year = int(input('Enter the year for checking ,year is leap or not:'))
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print('Entered year is a Leap Year')
        else:
            print('Entered year is not a Leap year')
    else:
        print('Entered Year is a Leap Year')
else:
    print('Entered year is not a Leap Year')
