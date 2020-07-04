# example 1:
multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
print(multiples)

# short way (list comprehensions)

another_multiples = [x * 7 for x in range(1, 11)]
print(another_multiples)

# example 2:
languages = ['Python', 'Perl', 'Ruby', 'Go', 'Java', 'C']
lengths = [len(language) for language in languages]
print(lengths)

# example 3:
z = [x for x in range(0, 101) if x % 3 == 0]
print(z)

# note: List-specific operations and methods
# list[i] = x Replaces the element at index i with x
# list.append(x) Inserts x at the end of the list
# list.insert(i, x) Inserts x at index i
# list.pop(i) Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
# list.remove(x) Removes the first occurrence of x in the list
# list.sort() Sorts the items in the list
# list.reverse() Reverses the order of items of the list
# list.clear() Removes all the items of the list
# list.copy() Creates a copy of the list
# list.extend(other_list) Appends all the elements of other_list at the end of list
