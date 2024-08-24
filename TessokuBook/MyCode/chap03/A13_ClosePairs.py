n, k = map(int, input().split())
a = list(map(int, input().split()))

delta = [i for i in range(1, n+1)]
count = 0
for i in range(1, n):
    if a[i] - a[0] > k:
        delta[0] = i - 1
        break
    if i == n - 1:
        delta[0] = n - 1
count += delta[0]

for i in range(1, n):
    if delta[i - 1] == n - 1:
        delta[i] = n - 1
        count += delta[i] - i
        continue

    for j in range(delta[i - 1] + 1, n):
        # print(i, j)
        # print(j)
        if a[j] - a[i] > k:
            delta[i] = j - 1
            break
        if j == n - 1:
            delta[i] = n - 1
    count += delta[i] - i
# print(delta)
print(count)
