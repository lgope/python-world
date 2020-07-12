# Python World
All about python. The goal of this repo is to save my all python code. 🙂👨‍💻

### Table of Contents
| No. | Contents |
| --- | --------- |
|1  | [Bool](####Bool) |
|2  | [Prime Number](####Prime-Number) |
|3  | [Palindrome](####Palindrome) |

#### Bool
`* You only need to pass the value as the argument, like this:`
```python
>>> bool(5)
True
>>> bool(0)
False
>>> bool([])
False
>>> bool({5, 5})
True
>>> bool(-5)
True
>>> bool(0.0)
False
>>> bool(None)
False
>>> bool(1)
True
>>> bool(range(0))
False
>>> bool(set())
False
>>> bool({5, 6, 2, 5})
True
```
**[⬆ Back to Top](#Python-World)**

#### Prime Number
```python
import math

print(int(math.sqrt(20)))

user_num = int(input('Enter an number: '))


def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


for i in range(2, user_num + 1):
    if is_prime(i):
        print(i)
```
**[⬆ Back to Top](#Python-World)**

#### Palindrome
```python
def palindrome(num):
    return str(num) == str(num)[::-1]


print(palindrome(99)) # True
print(palindrome(434)) # True
print(palindrome(929)) # True
print(palindrome(10001)) # True
print(palindrome(989889)) # False
```
**[⬆ Back to Top](#Python-World)**
