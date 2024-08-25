n, a = map(int, input().split())
t = list(map(int, input().split()))

waiting = []
currentTime = 0
for i in range(n):
    if t[i] < currentTime:
        currentTime += a
    else:
        currentTime = t[i] + a
    print(currentTime)
