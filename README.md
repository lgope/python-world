# Python World
All about python. The goal of this repo is to save my all python code. 🙂👨‍💻

### Table of Contents
| No. | Contents |
| --- | --------- |
|1  | [Variables](####variables) |
|2  | [Data Types](####aata-types) |
|3  | [Bool](####bool) |
|4  | [If Else](####if-else) |
|5  | [For Loop](####for-loop) |
|6  | [Function](####function) |
|7  | [Prime Number](####prime-number) |
|8  | [Palindrome](####palindrome) |

#### Variables
```python
num_coconuts = 2
print(f'I have  {str(num_coconuts)} coconuts')

num_coconuts = 9
print(f'I bought 9 coconuts and now have {str(num_coconuts)}')

num_coconuts += 11
print(f'I was given 11 coconuts and now I have {str(num_coconuts)}')

num_coconuts -= 2
print(f'I gave 2 coconuts away and now I have {str(num_coconuts)}')

num_coconuts = 'banana'
print(f'My coconuts turned into {num_coconuts}')

num_bananas = 5
print(f'What is happening to my coconuts? {num_coconuts * num_bananas}')

del num_coconuts
print(f"My coconuts don\'t exist anymore {str(num_coconuts)}")
```

**[⬆ Back to Top](#Python-World)**

#### Data Types
```python
# Fundamental Data Types
# int, float, bool, str, list, tuple, set, dict, complex

# Specialized Data Types
# None

# int and float
# print(type(6))
# print(type(2 - 4))
# print(type(2 * 4))
# print(type(2 / 4))


# print(type(2 ** 4))
# print(type(5 // 4))
# print(type(6 % 4))

print(7 / 4)  # 1.75
print(7 // 4)  # 1

# bin()
print(bin(5))  # binary of 5 0b101
print(int('0b101', 2))  # binary to int '5'

# The built-in Python function id() returns an object’s integer identifier. Using the id() function,
# you can verify that two variables indeed point to the same object


m = n = 88

print(m, n)
print(id(m))
print(id(n))

# str
strvalue = 'Hello World'
print(type(strvalue))

# complex
complexValue = 1j
print(type(complexValue))

# list
listValue = ["apple", "mango", "cherry"]
print(type(listValue))

# tuple
tupleValue = ("apple", "mango", "cherry")
print(type(tupleValue))

# dict
dictValue = {"name": "Lakshman", "age": 20}
print(type(dictValue))

# set
setValue = {"apple", "mango", "cherry"}
print(type(setValue))

# bytes
bytesValue = b"Hello World"
print(type(bytesValue))

# bool
boolValue = True
print(type(boolValue))

# some example
print(type(1))
print(type(3.14))
print(type('papaya'))
print(type(True))
print(type(False))
print(type(None))
print(type([1, 2, 10]))
print(type({'apple': 'A round fruit', 'banana': 'A long yellow fruit',
            'cucumber': 'A long green fruit'}))
```

**[⬆ Back to Top](#Python-World)**

#### Bool
`* You only need to pass the value as the argument, like this:`
```python
>>> bool(5)
True
>>> bool(0)
False
>>> bool([])
False
>>> bool({5, 5})
True
>>> bool(-5)
True
>>> bool(0.0)
False
>>> bool(None)
False
>>> bool(1)
True
>>> bool(range(0))
False
>>> bool(set())
False
>>> bool({5, 6, 2, 5})
True
```

**[⬆ Back to Top](#Python-World)**

#### If Else
```python
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
```

**[⬆ Back to Top](#Python-World)**

#### For Loop
```python
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
```

**[⬆ Back to Top](#Python-World)**

#### Function
```python
def add(a, b):
    return a + b


def say_hello(name, capitalize=False):
    if capitalize:
        name = name.upper()
    return 'Hello ' + name


print(say_hello('lakshman'))
print(say_hello('lakshman', True))
```

**[⬆ Back to Top](#Python-World)**

#### Prime Number
```python
import math

print(int(math.sqrt(20)))

user_num = int(input('Enter an number: '))


def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


for i in range(2, user_num + 1):
    if is_prime(i):
        print(i)
```
**[⬆ Back to Top](#Python-World)**

#### Palindrome
```python
def palindrome(num):
    return str(num) == str(num)[::-1]


print(palindrome(99)) # True
print(palindrome(434)) # True
print(palindrome(929)) # True
print(palindrome(10001)) # True
print(palindrome(989889)) # False
```
**[⬆ Back to Top](#Python-World)**
