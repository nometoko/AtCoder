n, m = map(int, input().split())
a = list(map(int, input().split()))

sum_a = [0] * (n + 1)
count_a = [0] * m
ans = 0
amari_sum = sum(a) % m

for i in range(n):
    sum_a[i + 1] = (sum_a[i] + a[i - 1]) % m
    tmp = (sum_a[i + 1] - amari_sum) % m
    ans += count_a[tmp]
    count_a[sum_a[i + 1]] += 1
    # print(count_a, sum_a[i + 1], i, tmp, ans)

for i in range(m):
    ans += count_a[i] * (count_a[i] - 1) // 2
print(ans)
