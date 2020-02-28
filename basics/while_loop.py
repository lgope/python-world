x = 4

while x >= 0:  # Will keep looping until condition is met
    print(x)
    x = x - 1

print()

y = 1
while True:  # Will keep looping until it encounters a break
    print(y)
    y += 1
    if y == 10:
        break

i = 0
while i < 10:
    print(i)
    i += 1
    # break
else:
    print('Done with all the work!')
