def recursion(ans, depth):
    if depth == n - 1:
        sum_ans = sum(ans)
        for i in range(1, r[depth] + 1):
            if (sum_ans + i) % k == 0:
                print(*ans, i)
    else:
        for i in range(1, r[depth] + 1):
            recursion(ans + [i], depth + 1)

n, k = map(int, input().split())
r = list(map(int, input().split()))
recursion([], 0)
