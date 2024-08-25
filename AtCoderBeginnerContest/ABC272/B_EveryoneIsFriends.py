n,m = map(int,input().split())

cnt = list([0 for _ in range(n)]for _ in range(n))

for i in range(m):
    a = list(map(int,input().split()))
    for j in a[1:]:
        for k in a[1:]:
            cnt[j-1][k-1] += 1
l = 0
for j in cnt:
    if 0 in j:
        print("No")
        l = 1
        break
if l == 0:
    print("Yes")