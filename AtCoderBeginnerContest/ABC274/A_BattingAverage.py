a, b = map(int, input().split())
ans = str(round(b / a, 3))
print(ans + '0' * (5 - len(ans)))
