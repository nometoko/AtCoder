s, t = input().split()


for i in range(1, len(s)):
    tmp = [s[j * i:min(j * i + i, len(s))] for j in range(len(s) // i + 1)]
    # print(*tmp)
    for j in range(i):
        if len(tmp[-1]) > j:
            # print(''.join([tmp[k][j] for k in range(len(tmp))]))
            if ''.join([tmp[k][j] for k in range(len(tmp))]) == t:
                print('Yes')
                exit(0)
        else:
            # print(''.join([tmp[k][j] for k in range(len(tmp) - 1)]))
            if ''.join([tmp[k][j] for k in range(len(tmp) - 1)]) == t:
                print('Yes')
                exit(0)
print('No')
