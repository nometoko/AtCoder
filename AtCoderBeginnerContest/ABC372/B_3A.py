import math
m = int(input())

ans = []
while m != 0:
    tmp = min(10, int(math.log(m, 3)))
    ans.append(tmp)
    m -= 3 ** tmp

print(len(ans))
print(*ans)
