n = int(input())
a = list(map(int, input().split()))
delta = [0] * (n + 1)

for i in range(1, n + 1):
    if a[i - 1] == 1:
        delta[i] = delta[i - 1] + 1
    else:
        delta[i] = delta[i - 1] - 1

# print(delta)
q = int(input())
for _ in range(q):
    left, right = map(int, input().split())
    if delta[right] - delta[left - 1] > 0:
        print('win')
    elif delta[right] - delta[left - 1] < 0:
        print('lose')
    else:
        print('draw')
