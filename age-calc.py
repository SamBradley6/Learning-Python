import datetime

date = datetime.datetime.now()

print('When were you born?')
year = int(input('Year(YYYY) '))
month = int(input('Month(MM) '))
day = int(input('Day(DD) '))

age_years = (date.year - year)
hadBirthday = f'You are {age_years}'
notHadBirthday = f'You are {age_years - 1}'

print(hadBirthday)
print(notHadBirthday)

if month > date.month: {
        print(notHadBirthday)
}
elif month == date.month & day > date.day: {
        print(notHadBirthday)
}
else: {
    print(hadBirthday)
}