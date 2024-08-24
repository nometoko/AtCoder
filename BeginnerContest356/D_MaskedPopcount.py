n, m = map(int, input().split())
div = 998244353
binM = bin(m)[2:]
binM = binM[::-1]
ans = 0
for i in range(len(binM)):
    if binM[i] == '1':
        count = (n + 1) // (2 ** (i + 1))
        ans += count * (2 ** i)
        tmp = n - (count * (2 ** (i + 1)) + 2 ** i - 1)
        if tmp > 0:
            ans += tmp
        # print(i, ans, count)
        ans = ans % div

print(ans)
