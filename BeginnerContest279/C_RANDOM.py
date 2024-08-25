h,w = map(int,input().split())
s = []
t = []
for _ in range(h):
    s.append(list(input()))
for _ in range(h):
    t.append(list(input()))
#print(*s)
ssub = []
tsub = []
for i in range(w):
    ssub.append(list(s[j][i] for j in range(h)))
    tsub.append(list(t[j][i] for j in range(h)))
cnt = 0
ssub.sort()
tsub.sort()
for i in range(w):
    if ssub[i] != tsub[i]:
        print("No")
        cnt = 1
        break
if cnt == 0:
    print("Yes")