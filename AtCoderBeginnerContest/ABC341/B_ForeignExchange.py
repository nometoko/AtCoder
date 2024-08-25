n = int(input())
a = list(map(int, input().split()))


for i in range(1, n):
    s, t = map(int, input().split())
    a[i] += a[i - 1] // s * t

print(a[-1])
