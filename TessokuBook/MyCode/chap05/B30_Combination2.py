h, w = map(int, input().split())
# (h + w - 2)C(h - 1)を求める
div = int(1e9 + 7)

# (h + w - 2)!
a = 1
for i in range(2, h + w - 1):
    a = a * i % div

b = 1
# (h - 1)!
for i in range(2, h):
    b = b * i % div

# (h - 1)!(w - 1)!
for i in range(2, w):
    b = b * i % div

# a / b % div = a * (b ^ (div - 2)) % div)
binDiv = bin(div - 2)[2:]
maximum = len(binDiv)
binDiv = binDiv[::-1]

bm = [0] * maximum
bm[0] = b
for i in range(1, maximum):
    bm[i] = bm[i - 1] ** 2 % div

ans = 1
for i in range(maximum):
    if binDiv[i] == '1':
        ans = ans * bm[i] % div
print(a * ans % div)
