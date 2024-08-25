import bisect

n = int(input())
a = list(map(int,input().split()))

b = sorted(set(a))
len_b = len(b)
count = [0] * n
for i in a:
    ind = bisect.bisect_right(b, i)
    sum = len_b - ind
    count[sum] += 1

for tmp in count:
    print(tmp)
