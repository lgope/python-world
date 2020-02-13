# add
add = lambda a : a + 10

print(add(5))

sum = lambda a, b, c = 4 : print(f'{a} + {b} + {c} = {a + b + c}')

sum(4, 5, 5)

# multiply
multiply = lambda a, b : a * b

print(f'multiply of 5 and 6 =  {multiply(5, 6)}')


# Lambda Functions
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
anotherdoubler = myfunc(4)

print(mydoubler(11))
print(anotherdoubler(4))
