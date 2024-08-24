d = int(input())
n = int(input())

delta = [0] * d
for i in range(n):
    # LeftRight.append(list(map(int, input().split())))
    left, right = map(int, input().split())
    delta[left - 1] += 1
    if right != d:
        delta[right] -= 1

t = 0
for i in delta:
    t = t + i
    print(t)
