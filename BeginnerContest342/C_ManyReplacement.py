import string
from collections import deque
n = int(input())
s = input()
replace = dict()
for i in string.ascii_lowercase:
    replace[i] = i

q = int(input())
for _ in range(q):
    a, b = input().split()
    for i in replace:
        if replace[i] == a:
            replace[i] = b

newString = []
for i in s:
    newString.append(replace[i])

print(*newString, sep='')
