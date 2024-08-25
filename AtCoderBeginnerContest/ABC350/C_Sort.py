
n = int(input())
a = list(map(int, input().split()))

ans = []
for i in range(n):
    while a[i] != i + 1:
        ans.append([min(i + 1, a[i]), max(a[i], i + 1)])
        tmp = a[a[i] - 1]
        a[a[i] - 1] = a[i]
        a[i] = tmp
    # print(i, a)

print(len(ans))
for i in ans:
    print(*i)
