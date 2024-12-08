import re

s = input()

index = 0
for i in range(1, len(s)):
    if s[i] == '|':
        print(i - index - 1, end=' ')
        index = i

print()
