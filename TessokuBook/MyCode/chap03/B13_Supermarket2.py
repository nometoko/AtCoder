n, k = map(int, input().split())
a = list(map(int, input().split()))

sumMoney = [0] * (n + 1)

for i in range(1, n + 1):
    sumMoney[i] = sumMoney[i - 1] + a[i - 1]

delta = [i for i in range(1, n + 1)]
count = 0
for i in range(1, n + 1):
    if sumMoney[i] > k:
        delta[0] = i - 1
        break
    if i == n:
        delta[0] = n
count += delta[0]

for i in range(1, n):
    if delta[i - 1] == n:
        delta[i] = n
        count += delta[i] - i
        continue
    for j in range(delta[i - 1], n + 1):
        if sumMoney[j] - sumMoney[i] > k:
            delta[i] = j - 1
            break
        if j == n:
            delta[i] = n
    count += delta[i] - i

# print(sumMoney)
# print(delta)
print(count)
