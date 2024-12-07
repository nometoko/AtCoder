n = int(input())

t = 0
sum = 0
for i in range(n):
    preT = t
    t, v = map(int, input().split())
    sum = max(0, sum - (t - preT))
    sum += v

print(sum)
