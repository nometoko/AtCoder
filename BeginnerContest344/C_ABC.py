from itertools import product

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = sorted(list(map(int, input().split())))
l = int(input())
c = sorted(list(map(int, input().split())))
q = int(input())
x = list(map(int, input().split()))

numList = set([i + j + k for i, j, k in product(a, b, c)])
i = 0

for i in x:
    if i in numList:
        print('Yes')
    else:
        print('No')
