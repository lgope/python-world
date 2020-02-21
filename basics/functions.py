def add(a, b):
    return a + b


def say_hello(name, capitalize=False):
    if capitalize:
        name = name.upper()
    return 'Hello ' + name


print(say_hello('lakshman'))
print(say_hello('lakshman', True))
