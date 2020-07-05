# dict are mutable (add, remove, replace are allowed)

file_counts = {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}
print(file_counts)

print(file_counts['txt'])

print('jpg' in file_counts)

print('html' in file_counts)

file_counts['cfg'] = 8

print(file_counts)

file_counts['csv'] = 17
print(file_counts)

del file_counts['cfg']

# print only keys
for extension in file_counts:
    print(extension)

# print items
for ext, amount in file_counts.items():
    print(f"There are {amount} files with the .{ext} extensions.")

# keys 
print(file_counts.keys())

# values
print(file_counts.values())


for value in file_counts.values():
    print(value)

# letters count
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("adsaasa"))
print(count_letters("a long string with a lot of letters"))


# list ()
# vs 
# dict (We want to use dictionaries when we plan on searching for a specific element)
ip_address = ["192.168.1.1", "127.0.0.1", "8.8.8.8"]

host_address = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}