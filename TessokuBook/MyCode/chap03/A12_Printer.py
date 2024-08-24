def paperNum(time, arr):
    paper = 0
    for i in arr:
        paper += time // i
    return paper


n, k = map(int, input().split())
a = list(map(int, input().split()))
maximum = n - 1
minimum = 0

t = int(1e10 // 2)
while True:
    # print(t, maximum, minimum, paperNum(t, a), paperNum(t - 1, a), k)
    ans = paperNum(t, a)
    if paperNum(t - 1, a) < k <= ans:
        break
    if ans >= k:
        maximum = t
        t = int((minimum + t) // 2)
    else:
        minimum = t
        t = int((t + maximum) // 2) + 1
print(t)
