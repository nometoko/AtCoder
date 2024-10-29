n, c = map(int, input().split())

t = list(map(int, input().split()))

prev = t[0]
count = 1
for i in range(1, n):
    if t[i] - prev >= c:
        count += 1
        prev = t[i]

print(count)
