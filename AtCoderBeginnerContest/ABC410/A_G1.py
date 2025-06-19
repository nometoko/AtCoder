n = int(input())
a = list(map(int, input().split()))
k = int(input())

a.sort()

cnt = 0
for i in a:
    if i >= k:
        cnt += 1

print(cnt)
