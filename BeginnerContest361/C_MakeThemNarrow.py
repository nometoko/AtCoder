# https://atcoder.jp/contests/abc361/tasks/abc361_c

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

min_index = 0
max_index = n - 1

min_diff = float('inf')
for i in range(k + 1):
    min_diff = min(min_diff, a[i + n - k - 1] - a[i])

print(min_diff)
