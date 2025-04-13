import numpy as np

def check(s, t):
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i][j] != t[i][j]:
                return False
    return True

n, m = map(int, input().split())

s = []
for _ in range(n):
    s.append(list(input()))

t = []
for _ in range(m):
    t.append(list(input()))

for i in range(n - m + 1):
    for j in range(n - m + 1):
        BREAK = False
        for k in range(m):
            for l in range(m):
                if s[i + k][j + l] != t[k][l]:
                    BREAK = True
                    break
            if BREAK:
                break
        if not BREAK:
            print(i + 1, j + 1)
            exit()
