n = int(input())
i = 0
if n <= 10:
    print(n - 1)
    exit(0)
else:
    n -= 1
n_pre = n
while n > 0:
    n_pre = n
    n -= 9 * 10 ** (i // 2)
    i += 1

n = n_pre - 1
n_str = str(n)
i -= 1
n_str = '0' * (i // 2 + 1 - len(n_str)) + n_str
ans = 10 ** i + 1
for j in range(len(n_str)):
    if i % 2 == 0 and i // 2 == j:
        ans += int(n_str[j]) * (10 ** j)
    else:
        ans += int(n_str[j]) * (10 ** j)
        ans += int(n_str[j]) * (10 ** (i - j))
print(ans)
