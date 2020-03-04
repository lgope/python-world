# add
add = lambda a: a + 10

print(add(5))

sum = lambda a, b, c=4: print(f'{a} + {b} + {c} = {a + b + c}')

sum(4, 5, 5)

# multiply
multiply = lambda a, b: a * b

print(f'multiply of 5 and 6 =  {multiply(5, 6)}')


# Lambda Functions
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
anotherdoubler = myfunc(4)

print(mydoubler(11))
print(anotherdoubler(4))

# Python lambda demo to use map() for adding elements of two lists

alist = ['learning', 'python', 'step', 'by', 'step']

output = list(map(lambda x: x.upper(), alist))

# Output: ['LEARN', 'PYTHON', 'STEP', 'BY', 'STEP']
print(output)

# Python lambda demo to filter out vowles from a list

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
vowels = ['a', 'e', 'i', 'o', 'u']

output = list(filter(lambda x: (x in vowels), alphabets))

# Output: ['a', 'e', 'i']
print(output)
