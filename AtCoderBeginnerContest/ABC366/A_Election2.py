n, t, a = map(int, input().split())
rest = n - t - a
if min(t, a) + rest < max(t, a):
    print('Yes')
else:
    print('No')
