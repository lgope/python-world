# add
add = lambda a : a + 10

print(add(5))


# multiply
multiply = lambda a, b : a * b

print(multiply(5, 6))


# Lambda Functions
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
anotherdoubler = myfunc(4)

print(mydoubler(11))
print(anotherdoubler(4))
