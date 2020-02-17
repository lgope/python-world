basket = [1, 2, 3, 4, 5]

# adding
# basket.append(90)
# basket.insert(5, 80)  # index, value
# basket.extend([100, 200])

# print(basket)

# coping
another_basket = basket.copy()
# print(another_basket)

# indexing
new_basket = ['a', 'a', 'z', 'b', 'c', 'd', 'e', 'd']
print('b' in new_basket)
print(new_basket.count('a'))

# sorting
print(sorted(new_basket))  # sorted() method produces new list/array

new_basket.sort()  # .sort() doesn't return any new list or array
print(new_basket)

# reversing
new_basket.reverse()
print(new_basket)

# removing
# basket.pop()
# basket.pop(1) # index number
# basket.remove(5) # value of the list
# basket.clear() # clear the list
# print(basket)

# range
print(list(range(1, 100)))

# join()

sentence = ' '.join(['hi', 'my', 'name', 'is', 'Lakshman'])
# print(sentence)

# list unpacking
a, b, c, *other, last_item = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a)
print(b)
print(c)
print(other)
print(last_item)
