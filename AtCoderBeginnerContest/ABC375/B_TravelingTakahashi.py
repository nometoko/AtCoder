def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

n = int(input())
totalDist = 0
initX, initY = 0, 0
preX, preY = initX, initY
for i in range(n):
    x, y = map(int, input().split())
    totalDist += distance(preX, preY, x, y)
    preX, preY = x, y

totalDist += distance(initX, initY, x, y)
print(totalDist)
