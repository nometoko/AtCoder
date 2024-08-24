n = int(input())
s = input()

sLen = len(s)
dp = [[0] * sLen for i in range(sLen)]

for i in range(sLen):
    dp[i][i] = 1
    j = i
    while j < sLen:
        if s[i] == s[j]:
            dp[i][j] = j - i + 1
            j += 1
        else:
            break

for length in range(1, sLen):
    for left in range(len(s) - length):
        right = left + length
        if dp[left][right] != 0:
            continue
        if s[left] == s[right]:
            dp[left][right] = max(dp[left + 1][right], dp[left][right - 1], dp[left + 1][right - 1] + 2)
        else:
            dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])

print(dp[0][-1])
