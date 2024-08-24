import numpy as np
import math
import itertools

def check(string, k):
    for i in range(n - k + 1):
        string_tmp = string[i:i+k]
        if string_tmp == string_tmp[::-1]:
            return False
    return True

n, k = map(int, input().split())
s = input()

letters = list(s)
letters_set = set(letters)
cnt = 0
for char in letters_set:
    cnt += s.count(char) // 2

if cnt < k // 2:
    ans = math.factorial(n)
    for char in letters_set:
        ans //= math.factorial(s.count(char))
    print(ans)
    exit(0)

strings = set(itertools.permutations(letters))
ans = 0
for string in strings:
    if check(string, k):
        ans += 1
print(ans)
