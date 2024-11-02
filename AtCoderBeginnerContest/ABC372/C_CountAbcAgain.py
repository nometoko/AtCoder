import bisect

DEBUG = False
n, q = map(int, input().split())
s = list(input())

index = []
for i in range(n - 2):
    if ''.join(s[i:i + 3]) == 'ABC':
        index.append(i)
ans = len(index)
for _ in range(q):
    x, c = input().split()
    x = int(x) - 1
    s[x] = c
    if DEBUG:
        print(x + 1, c)
        print(s, index)
    min_index = max(0, x - 2)
    max_index = min(n, x + 3)
    tmp_s = ''.join(s[min_index: max_index])
    if DEBUG:
        print(tmp_s)
    if len(index) != 0:
        tmp = bisect.bisect_right(index, x) - 1
        if DEBUG:
            print('tmp', tmp)
        if min_index <= index[tmp] <= max_index:
            exchange = False
            for i in range(len(tmp_s) - 2):
                if tmp_s[i:i + 3] == 'ABC':
                    index[tmp] = i + min_index
                    exchange = True
                    break
            if not exchange:
                index.pop(tmp)
                ans -= 1
        else:
            for i in range(len(tmp_s) - 2):
                if tmp_s[i:i + 3] == 'ABC':
                    index.insert(tmp + 1, i + min_index)
                    ans += 1
                    break
    else:
        for i in range(len(tmp_s) - 2):
            if tmp_s[i:i + 3] == 'ABC':
                index.append(i + min_index)
                ans += 1
                break
    print(ans)
