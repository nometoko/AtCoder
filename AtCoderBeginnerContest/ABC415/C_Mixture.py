def set_bit(num, digit):
    return num | (1 << digit)


def clear_bit(num, digit):
    return num & ~(1 << digit)


forward_set = set()
backward_set = set()


def bfs(state: int, n, s):
    # print(f"state = {bin(state)[2:].zfill(n)}, {state}, {s[state - 1]}")
    # if all charcters are used
    state = 0
    waiting = [set() for _ in range(n + 1)]
    waiting[0].add(state)

    for i in range(n):
        for state in waiting[i]:
            for j in range(n):
                # if the i-th character is not used
                if not (state & (1 << j)):
                    new_state = set_bit(state, j)
                    # print(new_state, bin(new_state)[2:].zfill(n), i, j)
                    if s[new_state - 1] == "0":
                        waiting[i + 1].add(new_state)

    # print(waiting)
    if len(waiting[-1]) > 0:
        return True
    else:
        return False


def dfs_back(state: int, n, s):
    if state > 0 and s[state - 1] == "1":
        return

    bit_count = state.bit_count()
    if bit_count == n // 2:
        backward_set.add(state)

    for i in range(n):
        if state & (1 << i):
            next_state = clear_bit(state, i)
            dfs_back(next_state, n, s)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    if bfs(0, n, s):
        print("Yes")
    else:
        print("No")
