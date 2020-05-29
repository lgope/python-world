with open("shakespeare_king_claudius.txt", mode="r") as shakespeare_file:
    all_words = []
    # unique_words = set()  # in set duplicate values not allowed!
    for line in shakespeare_file.readlines():
        words = line.strip().split(' ')
        all_words += words

    unique_words = set(all_words)
    print(f'Total words: {len(all_words)}')
    print(f'Unique words: {len(unique_words)}')

    with open("unique_words.txt", mode='w') as write_file:
        for word in sorted(unique_words):
            write_file.write(f'{word}\n')


print('Done!')
