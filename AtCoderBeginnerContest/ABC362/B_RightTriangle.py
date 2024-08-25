import numpy as np

xa = list(map(int, input().split()))
xb = list(map(int, input().split()))
xc = list(map(int, input().split()))

ab = (xa[0] - xb[0]) ** 2 + (xa[1] - xb[1]) ** 2
bc = (xb[0] - xc[0]) ** 2 + (xb[1] - xc[1]) ** 2
ca = (xc[0] - xa[0]) ** 2 + (xc[1] - xa[1]) ** 2
dist = [ab, bc, ca]
dist.sort()

if dist[2] == dist[0] + dist[1]:
    print('Yes')
else:
    print('No')
