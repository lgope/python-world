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

# temp = int(input("What temperature is your water: "))
temp = 11
if temp < 0:
    print("It's freezing! 🥶")
elif temp > 100:
    print("It's boiling and very hot ♨")
else:
    print("It's just normal water")

# another example
is_magician = True
is_expert = True

if is_expert and is_magician:
    print('You are a master magician!')
elif is_magician and not is_expert:
    print("At least you're getting there!")
elif not is_magician:
    print("You need magic powers!")
