h, w = map(int,input().split())
a = []
cnt = 0
for i in range(h):
    a.append(input())

for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            cnt += 1
print(cnt)