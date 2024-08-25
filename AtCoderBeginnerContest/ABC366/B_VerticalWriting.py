n = int(input())
s = []
len_s = []
for i in range(n):
    s.append(input())
    len_s.append(len(s[i]))

max_len = max(len_s)
for i in range(max_len):
    cnt = 0
    for j in range(n - 1, -1, -1):
        if i < len_s[j]:
            if cnt > 0:
                print('*' * cnt, end='')
                cnt = 0
            print(s[j][i], end='')
        elif j != 0:
            cnt += 1
    print()

