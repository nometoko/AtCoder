from bisect import bisect_left, bisect_right

DEBUG = False

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    now = s[0]
    goal = s[-1]

    mid = sorted(s[1:-1])

    REACHABLE = True
    # start and goal
    cnt = 2

    if DEBUG:
        hist = [now]

    while now * 2 < goal:
        next_ind = bisect_right(mid, now * 2)

        if next_ind == 0:
            # If no element is greater than now * 2, we cannot proceed
            REACHABLE = False
            break

        if len(mid) == 0:
            next_now = now
        elif next_ind > len(mid):
            next_now = mid[-1]
        else:
            next_now = mid[next_ind - 1]

        if now >= next_now:
            REACHABLE = False
            break

        now = next_now
        cnt += 1

        if DEBUG:
            hist.append(now)

    if REACHABLE:
        if DEBUG:
            hist.append(goal)
            print(f"History: {hist}")
        print(cnt)
    else:
        print(-1)
