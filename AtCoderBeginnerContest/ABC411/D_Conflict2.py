from collections import deque

n, q = map(int, input().split())

queries = []
for _ in range(q):
    queries.append(input().split())

t = q - 1  # 0-indexed
i = 0
ans = deque()

while t >= 0:
    query = queries[t]

    q_type = int(query[0])
    p = int(query[1])
    # print(f"q_type = {q_type}, p = {p}, i = {i}")

    if q_type == 1 and i == p:
        i = 0
    elif q_type == 2 and i == p:
        ans.append(query[2])
    elif q_type == 3 and i == 0:
        i = p

    t -= 1

while ans:
    print(ans.pop(), end="")
print()
