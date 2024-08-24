t = int(input())
n = int(input())
delta = [0] * t
for i in range(n):
    left, right = map(int, input().split())
    delta[left] += 1
    if right != t:
        delta[right] -= 1
# print(*delta)
num = 0
for i in range(t):
    num += delta[i]
    print(num)
