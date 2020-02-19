thisset = {"apple", "banana", "cherry", "mango"}
print(thisset)

for item in thisset:
  print(item)


print("banana" in thisset)

thisset.add("orange")

print(thisset)

thisset.update(["orange", "mango", "grapes"])

print(thisset)

thisset.remove("banana")

print(thisset)

thisset.discard("banana")

print(thisset)


x = thisset.pop()

print(x)

print(thisset)

thisset.clear()

print(thisset)
