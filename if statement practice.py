weight = int(input("What is your weight?"))

unit = input("(L)bs or (K)g? ").upper()

if unit == "K":{
    print(f'Your weight is {round(weight * 2.205)}lbs')
}
elif unit == "L":{
    print(f'Your weight is {round(weight / 2.205)}kg')
}
else:{
    print("learn to read and try again")
}