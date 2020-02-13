numbers = [4, 6, 8, 10]
product = 1
for number in numbers:
    product *= number
    print(product)
print('The total product is:', product)


for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))