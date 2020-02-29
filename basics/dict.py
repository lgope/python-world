# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Hello', 2: 'World', 3: 'From', 4: 'Python!'}
print(Dict)

# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Python', 1: [1, 2, 3, 4], 2: [10, 20, 30, 40]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Hello', 2: 'World'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Hello'), (2, 'World!')])
print("\nDictionary with each item as a pair: ")
print(Dict)

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'mango'}

# dictionary with mixed keys
my_dict = {'name': 'Lakshman', 1: [2, 4, 3, 5]}

# using dict()
my_dict = dict({1: 'apple', 2: 'mango'})

# from sequence having each item as a pair
my_dict = dict([(1, 'apple'), (2, 'mango')])

MLB_team = dict(
    Colorado='Rockies',
    Boston='Lakshman',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)

print(MLB_team)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2020

for i in thisdict:
    print(i)
