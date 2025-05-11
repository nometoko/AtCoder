def count(pos, dist, c):
    # print(pos, dist)
    # print(f"from {pos} to {dist}", end=" ")
    cnt = 0
    reachable = pos

    while reachable > dist:
        pre_reachable = reachable
        for i in range(reachable, pos + 1):
            reachable = min(reachable, i - c[i])

        cnt += 1
        pos = pre_reachable - 1
    # print(f"takes {cnt} steps")
    return cnt


n = int(input())

c = list(map(int, input().split()))
a = list(map(int, input().split()))

cnt = 0

cup_with_beans = [-1]

for cup, num_beans in enumerate(a):
    if num_beans > 0:
        cup_with_beans.append(cup)

cup_with_beans.reverse()

ans = 0
for i in range(len(cup_with_beans) - 1):
    cup = cup_with_beans[i]
    next_cup = cup_with_beans[i + 1]
    ans += count(cup, next_cup, c)

print(ans)
