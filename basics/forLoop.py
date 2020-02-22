numbers = [4, 6, 8, 10]
product = 1
for number in numbers:
    product *= number
    print(product)
print('The total product is:', product)

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x * x * x).rjust(4))

# Use range() to loop through a list of numbers
for i in range(10):
    print(i)
print()

for i in range(10, 20):
    print(i)
print()

for i in range(10, 20, 2):
    print(i)
print()

primes = [1, 2, 3, 5, 7, 11, 13]
# Can loop over lists
for number in primes:
    print(number)

# If you need to know the index, use enumerate()
for i, number in enumerate(primes):
    print(f'{i}: {number}')
