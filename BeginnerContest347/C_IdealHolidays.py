n, a, b = map(int, input().split())
d = list(map(int, input().split()))

for i in range(n):
    d[i] = int(d[i] % (a + b))

d = list(set(d))
d.sort()
for i in range(len(d) - 1):
    if d[i + 1] - d[i] > b:
        for j in range(i + 1, len(d)):
            d[j] = d[j] - (a + b)
        break

if max(d) - min(d) < a:
    print("Yes")

else:
    print("No")
