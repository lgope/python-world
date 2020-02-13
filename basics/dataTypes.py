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
print(7 // 4) # 1

# bin()
print(bin(5)) # binary of 5 0b101
print(int('0b101', 2)) # binary to int '5'


# The built-in Python function id() returns an object’s integer identifier. Using the id() function, you can verify that two variables indeed point to the same object


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
tupleValue =("apple", "mango", "cherry")
print(type(tupleValue))

# dict
dictValue = {"name" : "Lakshman", "age" : 20}
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