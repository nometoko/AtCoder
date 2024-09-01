from functools import cache

@cache
def func(generation):
    if generation == 1:
        return 0
    return 1 + func(pare[generation])

n = int(input())
a = list(map(int, input().split()))
pare = dict()
for i in range(n):
    pare[2 * (i + 1)] = a[i]
    pare[2 * (i + 1) + 1] = a[i]

# print(pare)
for i in range(1, 2 * n + 2):
    print(func(i))
