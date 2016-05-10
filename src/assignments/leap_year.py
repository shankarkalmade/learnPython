

''' sample code to check entered year is leap or not'''

input_year = input("Enter year to validate leap year: ")

if (input_year % 4) == 0 :
    if (input_year%100) == 0:
        if(input_year % 400) == 0:
            print 'Entered Year : %s is leap year' % input_year
        else:
            print 'Entered Year : %s is not leap year' % input_year

    else:
        print 'Entered Year : %s is leap year' % input_year

else:
    print 'Entered Year : %s is not leap year' % input_year




