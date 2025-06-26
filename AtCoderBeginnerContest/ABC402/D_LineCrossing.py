n, m = map(int, input().split())

cnts = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    cnts[(a + b) % n] += 1

ans = int(m * (m - 1) / 2)

for cnt in cnts:
    ans -= int(cnt * (cnt - 1) / 2)

print(ans)
