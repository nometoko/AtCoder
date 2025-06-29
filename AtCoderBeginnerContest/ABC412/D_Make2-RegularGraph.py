from itertools import combinations

DEBUG = False


def add_node(paths, node, neighbour):
    paths[node].add(neighbour)
    paths[neighbour].add(node)


def remove_node(paths, node, neighbour):
    paths[node].remove(neighbour)
    paths[neighbour].remove(node)


def cnt_replace(original, ideal):
    ans = 0

    for i in range(1, len(original) + 1):
        ans += len(original[i] | ideal[i]) - len(original[i] & ideal[i])
    ans //= 2
    return ans


def search(node, current_path, original_path):
    if DEBUG:
        print(node, current_path, original_path)
    if node == len(current_path) + 1:
        ans = cnt_replace(current_path, original_path)
        if DEBUG:
            print(f"Current path: {current_path}")
            print(f"should replace: {ans}")
        return ans

    neighbours = [
        j for j in range(node + 1, len(current_path) + 1) if len(current_path[j]) < 2
    ]
    if DEBUG:
        print(f"Node: {node}, Neighbours: {neighbours}")

    ans = float("inf")

    if len(current_path[node]) < 2:
        if DEBUG:
            print(2 - len(current_path[node]), "neighbours needed")
        for neighbour in combinations(neighbours, 2 - len(current_path[node])):
            if DEBUG:
                print(f"Current node: {node}, Neighbours: {neighbour}")
            for next in neighbour:
                add_node(current_path, node, next)
            ans = min(ans, search(node + 1, current_path, original_path))
            for next in neighbour:
                remove_node(current_path, node, next)

    else:
        ans = search(node + 1, current_path, original_path)

    return ans


n, m = map(int, input().split())

paths = dict()
empty_paths = dict()

for i in range(1, n + 1):
    paths[i] = set()
    empty_paths[i] = set()

for _ in range(m):
    a, b = map(int, input().split())
    add_node(paths, a, b)


print(search(1, empty_paths, paths))
