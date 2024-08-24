n, r = map(int, input().split())

div = int(1e9 + 7)
a = 1
for i in range(2, n + 1):
    a = a * i % div

b = 1
for i in range(2, r + 1):
    b = b * i % div

for i in range(2, n - r + 1):
    b = b * i % div

maximum = len(bin(div)[2:]) + 1
bm = [0] * maximum
bm[0] = b

for i in range(1, maximum):
    bm[i] = bm[i - 1] ** 2 % div

binDiv = bin(div - 2)[2:]
binDiv = '0' * (maximum - len(binDiv)) + binDiv
binDiv = binDiv[::-1]

ans = 1
for i in range(maximum):
    if binDiv[i] == '1':
        ans = ans * bm[i] % div
print(a * ans % div)
