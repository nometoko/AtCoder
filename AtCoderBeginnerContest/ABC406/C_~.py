import bisect

n = int(input())
p = list(map(int, input().split()))

localMax = []
localMin = []
start = []

for i in range(len(p) - 1):
    if p[i + 1] > p[i]:
        start.append(i)

    if i >= 1:
        if p[i - 1] < p[i] > p[i + 1]:
            localMax.append(i)
        elif p[i - 1] > p[i] < p[i + 1]:
            localMin.append(i)

cnt = 0
if len(start) == 0 or len(localMax) == 0 or len(localMin) == 0:
    print(0)
    exit()

# print(localMax)
# print(localMin)

for s in start:
    maxInd = bisect.bisect_left(localMax, s)
    minInd = bisect.bisect_left(localMin, s)
    if maxInd > len(localMax) - 1 or minInd > len(localMin) - 1:
        break

    if localMax[maxInd] == s:
        maxInd += 1
    if localMin[minInd] == s:
        minInd += 1

    if maxInd > len(localMax) - 1 or minInd > len(localMin) - 1:
        break

    if localMax[maxInd] < localMin[minInd]:
        if maxInd < len(localMax) - 1 and localMax[maxInd + 1] < localMin[minInd]:
            continue
        else:
            if maxInd == len(localMax) - 1:
                nextMax = n - 1
            else:
                nextMax = localMax[maxInd + 1]
            if minInd == len(localMin) - 1:
                nextMin = n - 1
            else:
                nextMin = localMin[minInd + 1]

            nextInd = min(nextMax, nextMin)
            cnt += nextInd - localMin[minInd]
            # print(f"maxVal: {localMax[maxInd]}, minVal: {localMin[minInd]}")
            # print(
            #     f"nextMax: {nextMax}, nextMin: {nextMin}, nextInd: {nextInd}, cnt: {cnt}"
            # )

    else:
        if minInd < len(localMin) - 1 and localMax[maxInd + 1] < localMin[minInd]:
            continue
        else:
            if maxInd == len(localMax) - 1:
                nextMax = n - 1
            else:
                nextMax = localMax[maxInd + 1]
            if minInd == len(localMin) - 1:
                nextMin = n - 1
            else:
                nextMin = localMin[minInd + 1]
            nextInd = min(nextMax, nextMin)
            cnt += nextInd - localMin[minInd]
    # print(s, cnt)
print(cnt)
