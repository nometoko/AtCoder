# わかんなかったらAtCoderの一回目のACの提出を見るべし
import numpy as np

n = int(input())
pos = []
for _ in range(n):
    pos.append(list(map(int, input().split())))

dist = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        distance = np.linalg.norm(np.array(pos[i]) - np.array(pos[j]))
        dist[i][j] = distance
        dist[j][i] = distance


dp = [[np.infty] * n for _ in range(2 ** (n - 1))]

# 1個目の都市からの距離
for i in range(1, n):
    dp[0][i] = dist[0][i]

dp[0][0] = 0

# 1個目の都市は最後に訪れるので、考えるべき訪れた都市の組み合わせは2^(n-1)でよい
for i in range(2 ** (n - 1)):
    # 1個目は訪れていないので後ろに0つける
    binI = bin(i)[2:] + '0'
    binI = '0' * (n - len(binI)) + binI
    binI = binI[::-1]

    for j in range(1, n):
        if binI[j] == '1':
            continue
        # print(i, j, (i * 2 + 2 ** j) // 2)
        for k in range(n):
            # 都市Kを訪れていなかったら
            if binI[k] == '0' and j != k:
                dp[(i * 2 + 2 ** j) // 2][k] = min(dp[(i * 2 + 2 ** j) // 2][k], dp[i][j] + dist[j][k])

# for d in dp:
#     print(*d)

# 考えるのは、dp[01111....(2)][0]→1を訪れていなくて最後に訪れる時のdp
print(dp[-1][0])
