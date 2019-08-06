# century(1705), 18, 'Testing for year 1705'
# century(1900), 19, 'Testing for year 1900'
# century(1601), 17, 'Testing for year 1601'
# century(2000), 20, 'Testing for year 2000'
# century(356), 4, 'Testing for year 356'
# century(89), 1, 'Testing for year 89'

def century(year):
    if (year%100) ==0:
        yes = year//100
        print(yes)
        return yes
        

    else:
        no = (year//100)+1
        print(no)
        return no



century(1705)
century(1900)