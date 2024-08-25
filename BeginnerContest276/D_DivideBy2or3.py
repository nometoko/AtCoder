n = int(input())
a = list(map(int,input().split()))
anew = [[0] * 2 for _ in range(n)]

for i in range(len(a)):
    while a[i]%2==0:
        a[i] = int(a[i]/2)
        anew[i][0] += 1
    while a[i]%3==0:
        a[i] = int(a[i]/3)
        anew[i][1] += 1
ans = 0
if len(list(set(a))) == 1:
    for i in range(2):
        mini = min(anew[j][i] for j in range(n))
        for j in range(n):
            ans += anew[j][i] - mini
    print(ans)
else:
    print(-1)