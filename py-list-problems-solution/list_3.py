def reverse(item):
    return item[::-1]


def is_palindrome(item):
    rev = reverse(item)

    if item == rev:
        return True
    return False


sample_list = ['abc', 'xyz', 'aba', '1221']
res = 0
for i in range(0, len(sample_list)):
    if len(sample_list[i]) >= 2:
        if is_palindrome(sample_list[i]):
            res += 1
print(res)
