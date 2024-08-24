n = int(input())
ans = [0] * 10

for i in range(9, -1, -1):
    if n >= 2 ** i:
        ans[9 - i] = 1
        n -= 2 ** i

for i in ans:
    print(i, end='')
