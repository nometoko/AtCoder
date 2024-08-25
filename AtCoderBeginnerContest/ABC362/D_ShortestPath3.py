import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
path = [[] for _ in range(n)]
for i in range(m):
    u, v, b = map(int, input().split())
    path[u - 1].append([v - 1, b])
    path[v - 1].append([u - 1, b])

decided = [False] * n
dis = [float('inf')] * n
dis[0] = a[0]
Q = []
heapq.heappush(Q, (dis[0], 0))


def dijkstra(edges):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする """
    visited = [False] * n
    node = [float('inf')] * n  # スタート地点以外の値は∞で初期化
    node[0] = a[0]  # スタートは0で初期化

    node_name = []
    heapq.heappush(node_name, [a[0], 0])

    while len(node_name) > 0:
        # ヒープから取り出し
        _, min_point = heapq.heappop(node_name)
        if visited[min_point] is True:
            continue
        visited[min_point] = True
        # 経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[min_point]:
            goal = factor[0]  # 終点
            cost = factor[1]  # コスト
            if visited[goal] is False:
                tmp = node[min_point] + cost + a[goal]
                # 更新条件
                if tmp < node[goal]:
                    node[goal] = tmp  # 更新
                    heapq.heappush(node_name, [node[goal], goal])
    return node


opt_node = dijkstra(path)
for i in range(1, n):
    print(opt_node[i], end=' ')
