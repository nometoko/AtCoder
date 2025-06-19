n, q = map(int, input().split())
x = list(map(int, input().split()))

n_balls = [0] * n

for query in x:
    if query > 0:
        n_balls[query - 1] += 1
        print(query, end=" ")

    else:
        min_ball_ind = -1
        min_ball = float("inf")
        for i, n_ball in enumerate(n_balls):
            if n_ball < min_ball:
                min_ball = n_ball
                min_ball_ind = i

        n_balls[min_ball_ind] += 1
        print(min_ball_ind + 1, end=" ")

print()
