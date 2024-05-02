import datetime


date = datetime.datetime.now()


print('When were you born?')
yearasstring = input('Year(YYYY) ')
monthasstring = input('Month(MM) ')
dayasstring = input('Day(DD) ')

year = int(yearasstring)
month = int(monthasstring)
day = int(dayasstring)

age_years = (date.year - year)
if month > date.month: {
        print('Your age is: ' + str(age_years - 1))
}
elif month == date.month & day > date.day: {
        print("Your age is: " + str(age_years - 1))
}
elif month == date.month & day < date.day: {
        print('Your age is: ' + str(age_years))
}
else: {
    print('Your age is: ' + str(age_years))
}