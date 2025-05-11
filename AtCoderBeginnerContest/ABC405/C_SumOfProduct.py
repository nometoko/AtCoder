n = int(input())
a = list(map(int, input().split()))

sum_a = [0] * n
sum_a[0] = a[0]

for i in range(1, n):
    sum_a[i] = sum_a[i - 1] + a[i]

# print(sum_a)
ans = 0

for i in range(n - 1):
    ans += sum_a[i] * a[i + 1]
    # print(ans)

print(ans)
