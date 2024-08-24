a, b = map(int, input().split())
binB = bin(b)[2:]
benB = binB[::-1]

maximum = len(binB)
div = 10 ** 9 + 7
ab = [0] * maximum
ab[0] = a
for i in range(1, maximum):
    ab[i] = ab[i - 1] ** 2 % div

ans = 1
for i in range(maximum):
    if benB[i] == '1':
        ans = ans * ab[i] % div
print(ans)
