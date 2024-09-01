n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()
elif n == 2:
    print(3)
    exit()

diff = [0] * (n - 1)
for i in range(n - 1):
    diff[i] = a[i] - a[i + 1]

tmp = diff[0]
count = 1
ans = n

for i in range(1, n - 1):
    if diff[i] == tmp:
        count += 1
    else:
        ans += (1 + count) * count // 2
        tmp = diff[i]
        count = 1
ans += (1 + count) * count // 2
print(ans)
