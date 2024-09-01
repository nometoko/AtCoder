n = int(input())

l = -1
r = -1
ans = 0
for i in range(n):
    a, s = input().split()
    a = int(a)
    if s == "L":
        if l == -1:
            l = a
        else:
            ans += abs(a - l)
            l = a
    else:
        if r == -1:
            r = a
        else:
            ans += abs(a - r)
            r = a

print(ans)
