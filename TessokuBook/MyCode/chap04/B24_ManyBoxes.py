import bisect
n = int(input())
lengths = []
for i in range(n):
    lengths.append(list(map(int, input().split())))

lengths.sort()

vertical = [lengths[i][0] for i in range(n)]
l = [lengths[0][1]]
# verticalをもとにソートしているのでhorizontalだけ考えれば良い
for v in sorted(set(vertical)):
    # horizontalは大きい順にソート
    tmpHorizontal = reversed([lengths[i][1] for i in range(bisect.bisect_left(vertical, v), bisect.bisect_right(vertical, v))])
    for h in tmpHorizontal:
        index = bisect.bisect_left(l, h)
        if index == len(l):
            if l[-1] < h:
                l.append(h)
        else:
             l[index] = h

print(len(l))
