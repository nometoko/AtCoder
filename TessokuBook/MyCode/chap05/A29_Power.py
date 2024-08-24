a, b = map(int, input().split())
x = 1
maximum = 30
div = 10 ** 9 + 7
ab = [0] * maximum
ab[0] = a
for i in range(1, maximum):
    ab[i] = ab[i - 1] ** 2 % div

binB = bin(b)[2:]
binB = '0' * (maximum - len(binB)) + binB
benB = binB[::-1]
ans = 1
for i in range(maximum):
    if benB[i] == '1':
        ans *= ab[i]
print(ans % div)
