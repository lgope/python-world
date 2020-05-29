# Input Sample :
# Hello Test! 123 123, good.
# Output :
# HT
# elloestgood
# 123123
#  !  , .

str = input()
upperCaseLetter = ''
lowerCaseLetter = ''
numbers = ''
others = ''

for i in str:
    if i.isupper():
        upperCaseLetter += i
    elif i.islower():
        lowerCaseLetter += i
    elif i.isnumeric():
        numbers += i
    else:
        others += i

print(upperCaseLetter)
print(lowerCaseLetter)
print(numbers)
print(others)
