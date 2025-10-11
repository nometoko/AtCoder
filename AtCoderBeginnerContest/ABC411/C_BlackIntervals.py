n, q = map(int, input().split())
a_list = list(map(int, input().split()))

bw = [False] * n

ans = 0
for a in a_list:
    # 0-indexed
    a -= 1

    bw[a] = not bw[a]

    if n == 1:
        ans = 1 * bw[a]
    else:
        if a == n - 1:
            # white, white -> white, black
            if bw[a] is not bw[a - 1] and bw[a] is True:
                ans += 1
            # white, black -> white, white
            if bw[a] is bw[a - 1] and bw[a] is False:
                ans -= 1
        elif a == 0:
            # white, white -> white, black
            if bw[a] is not bw[a + 1] and bw[a] is True:
                ans += 1
            # black, white -> white, white
            if bw[a] is bw[a + 1] and bw[a] is False:
                ans -= 1
        else:
            if bw[a] == bw[a - 1] and bw[a] == bw[a + 1]:
                # white, black, white -> white, white, white
                # black, white, black -> black, black, black
                ans -= 1
            elif bw[a] != bw[a - 1] and bw[a] != bw[a + 1]:
                # white, white, white -> white, black, white
                # black, black, black -> black, white, black
                ans += 1

    print(ans)
