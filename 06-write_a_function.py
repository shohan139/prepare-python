# a function which returns true if the year is a leap year otherwise returns false
def is_leap(year):
    leap = False
    
    if year%100 == 0 and year%400 == 0:
        leap = True
    elif year%4 == 0:
        if year%100 !=0 and year%400 != 0:
            leap = True
    else:
        leap = False
    return leap
        

year = int(input())
print(is_leap(year))
