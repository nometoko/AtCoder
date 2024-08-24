n = int(input())

a = []
b = []
ans = 0
maxDiff = -1
for i in range(n):
    a, b = map(int, input().split())
    maxDiff = max(maxDiff, b - a)
    ans += a

print(ans + maxDiff)
