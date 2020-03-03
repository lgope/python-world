# 1. Looping over numbers:

result = []
for i in range(100):
     if  i% 5 == 0:
         result.append(i)

Final output: 
result = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# Better way

result = range(0,100,5)
# range(start, end, step)

# 2. Looping over a list

colours = ['red', 'green', 'blue', 'yellow']
for i in range(len(colours)):
     print colours[i]


# Better way

for colour in colours:
     print colour

# 3. Looping over a list and its idices

for i in range(len(colours)):
     print i, '-->', colours[i]

# Better way

for i, colour in enumerate(colours):
     print i, '-->', colour

# 4. Looping backwards

for i in range(len(colours), -1, -1, -1):
     print colours[i]

#  Better way

for colour in reversed(colours):
      print colour



# 5. sorting  in ascending order

for colour in sorted(colours):
     print colour


# 6. sorting in descending order

for colour in sorted(colours, reversed=True): 
     print colour


# 7. looping over two collections 

names = ['lakshman', 'raton', 'knowing']
colours = ['pink', 'green', 'blue', 'yellow']
n = min(len(colours), len(names))
for i in range(n):
     print names[i], '-->', colours[i]


# Better way

for name, colour in zip(names, colours):
      print name, '-->', colour


# 8. looping over dictionary keys and values

for key in dict:
    print key, '-->', d[key]


# Better way

for key, value in dict.items():
     print key, value

# Best way

for key, value  in dict.iteritems():
     print key, '-->', value 



# 10. construct a dictionary from two lists

names = ['Steve Jobs','Bill Gates ','Jeff Bezos']
org = ['Apple', 'Microsoft', 'Amazon']
d = dict(zip(names, org))

# Better way

from itertools import izip
d = dict(izip(names, org))


# 11. using comparison operator 

is_master = None
if role == 'master':
    is_master = True
else:
    is_master =  False


# Best way 

is_master = role == 'master'


# 12. achieve  switch/case in python with dict

def switch(case):
      cases = {1: 'case 1',
                    2: 'case 2',
                    3: 'case 3'}
         return cases.get(case, "default")


# 13. convert  a list of strings to numbers

str_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers = []
for i in str_numbers:
      numbers.append(int(i))

# Best way 

numbers = map(int, str_numbers)



# 14. multiplying numbers  a list of numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = 1
for num in numbers:
     result  *= num

# Best way is 

def multiply(a, b):
      return a*b
result = reduce(multiply, numbers)


# 15. finding multiples of 3  from a random set of numbers

numbers = [2, 7, 5, 4, 6, 1, 8, 9, 7, 3, 7, 5, 9, 3, 8, 4, 9, 6, 8, 5, 9, 7, 2, 6, 8, 8, 7, 6, 5, 9, 1, 1, 5, 5, 7, 4, 1, 0, 1, 1, 5, 4, 8, 4, 8, 7, 7, 8, 0, 1, 6, 8, 4]
list = []
for num in numbers:
      if num % 3 == 0:
            list.append( num )


# Better way is 

def devide3(n):
      return n%3 == 0
list = filter(devide3, numbers)










