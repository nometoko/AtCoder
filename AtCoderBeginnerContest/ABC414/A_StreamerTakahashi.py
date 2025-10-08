n, l, r = map(int, input().split())

cnt = 0
for _ in range(n):
    x, y = map(int, input().split())
    if x <= l and r <= y:
        cnt += 1

print(cnt)
