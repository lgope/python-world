space_range = 4
for row in range(1, 6):
    for space in range(space_range):
        print(' ', end=' ')
    for col in range(1, row + 1):
        print('*', end=' ')
    for col in range(row - 1):
        print('*', end=' ')
    print()
    space_range -= 1
