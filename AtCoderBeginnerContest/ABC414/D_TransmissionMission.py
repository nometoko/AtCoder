n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

diff = [x[i + 1] - x[i] for i in range(n - 1)]
diff.sort()
print(sum(diff[: n - m]))
