n = int(input())
d = list(map(int, input().split()))
sum_d = [0] * (n + 1)

for i, dist in enumerate(d):
    sum_d[i + 1] = sum_d[i] + dist

for i in range(n - 1):
    for j in range(i + 1, n):
        print(sum_d[j] - sum_d[i], end=" ")
    print()
