n, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

sweet = 0
salty = 0

for i in range(n):
    sweet += a[i]
    salty += b[i]
    if sweet > x:
        print(i + 1)
        exit(0)
    if salty > y:
        print(i + 1)
        exit(0)

print(n)
