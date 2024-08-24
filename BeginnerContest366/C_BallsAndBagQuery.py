q = int(input())
balls = [0] * (10 ** 6)
ans = 0
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
            balls[query[1] - 1] += 1
            if balls[query[1] - 1] == 1:
                ans += 1
    elif query[0] == 2:
        balls[query[1] - 1] -= 1
        if balls[query[1] - 1] == 0:
            ans -= 1
    else:
        print(ans)
