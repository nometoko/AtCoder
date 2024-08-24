n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0
vacant = k
for i in range(n):
    if vacant >= a[i]:
        vacant -= a[i]
    else:
        count += 1
        vacant = k - a[i]

# 最後の組
print(count + 1)
