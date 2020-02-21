salutation = 'Hello world'
shouting = False

if shouting:
    print(salutation.upper())
else:
    print(salutation)

hungry = True

if hungry:
    print('Find something to eat')
print('Continue your day')

temp = int(input("What temperature is your water: "))

if temp < 0:
    print("It's freezing! 🥶")
elif temp > 100:
    print("It's boiling and very hot ♨")
else:
    print("It's just normal water")
