# 0, R:ぐー, 1, S:ちょき, 2, P:ぱー

def janken(me, enemy):
    if me == 0:
        if enemy == 'R':
            return 0
        elif enemy == 'S':
            return 1
        elif enemy == 'P':
            return -1
    elif me == 1:
        if enemy == 'R':
            return -1
        elif enemy == 'S':
            return 0
        elif enemy == 'P':
            return 1
    elif me == 2:
        if enemy == 'R':
            return 1
        elif enemy == 'S':
            return -1
        elif enemy == 'P':
            return 0

def janken_dp(me, enemy, wins):
    result = janken(me, enemy)
    if result == 1:
        return wins + 1
    elif result == -1:
        return 0
    elif result == 0:
        return wins


n = int(input())
s = input()

dp = [[0]*3 for _ in range(n + 1)]

for i in range(1, n + 1):
    enemy = s[i - 1]    
    for pre_me in range(3):
        for me in range(3):
            if pre_me == me:
                continue
            dp[i][me] = max(dp[i][me], janken_dp(me, enemy, dp[i - 1][pre_me]))

print(max(dp[-1]))
