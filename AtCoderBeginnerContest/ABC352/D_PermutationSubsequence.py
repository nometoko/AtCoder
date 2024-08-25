# dequeで時間1/5程度になった
from collections import deque

# スライド最大値(最小値)
n, k = map(int, input().split())
p = list(map(int, input().split()))

orderList = [[p[i], i + 1] for i in range(n)]
orderList.sort()
newOrderList = [orderList[i][1] for i in range(n)]

# Initialize
maxDp = deque()
minDp = deque()
for i in range(0, k):
    while len(maxDp) > 0 and maxDp[-1] < newOrderList[i]:
        maxDp.pop()
    maxDp.append(newOrderList[i])

    while len(minDp) > 0 and minDp[-1] > newOrderList[i]:
        minDp.pop()
    minDp.append(newOrderList[i])

diff = maxDp[0] - minDp[0]
ans = diff

for i in range(1, n - k + 1):
    if newOrderList[i - 1] == maxDp[0]:
        maxDp.popleft()

    while len(maxDp) > 0 and maxDp[-1] < newOrderList[i + k - 1]:
        maxDp.pop()
    maxDp.append(newOrderList[i + k - 1])

    if newOrderList[i - 1] == minDp[0]:
        minDp.popleft()

    while len(minDp) > 0 and minDp[-1] > newOrderList[i + k - 1]:
        minDp.pop()
    minDp.append(newOrderList[i + k - 1])

    diff = maxDp[0] - minDp[0]
    if ans > diff:
        ans = diff
    if ans == k - 1:
        break

print(ans)
