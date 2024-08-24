s = input()
ans = [s[i:min(i+j, len(s))] for i in range(len(s)) for j in range(1, len(s) + 1)]
ans = list(set(ans))
print(len(ans))