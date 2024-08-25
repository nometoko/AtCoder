n = int(input())
a = list(map(int, input().split()))
order = [0] * n
orderSum = [0] * n
div = 998244353
order[0] = 10 ** len(str(a[0]))
orderSum[0] = a[0]
for i in range(1, n):
    order[i] = 10 ** len(str(a[i]))
    orderSum[i] = orderSum[i - 1] + order[i]

ans = 0
for i in range(n):
    ans += (orderSum[-1] - orderSum[i]) * a[i]
    ans += a[i] * i
    ans = ans % div

print(ans)
