a, b, c = map(int, input().split())

bin_c = bin(c)[2:]

one_count_binC = bin_c.count('1')

if (one_count_binC % 2 != abs(a - b) % 2) or (one_count_binC < abs(a - b)) or one_count_binC > (a + b):
    print(-1)

else:
    xy = [0, 0]
    i = 0
    one_binC_common = (one_count_binC - abs(a - b)) / 2
    zero_binC_common = min(a, b) - one_binC_common
    # print(one_binC_common, zero_binC_common, bin_c)
    while True:
        # print(len(bin_c), i, one_binC_common, zero_binC_common)
        if i < len(bin_c) and bin_c[-(1 + i)] == '1':
            if one_binC_common > 0:
                xy[int(one_binC_common * 2) % 2] += 2 ** i
                one_binC_common -= 0.5

            else:
                if a > b:
                    xy[0] += 2 ** i
                else:
                    xy[1] += 2 ** i
            # print(bin(xy[0])[2:], bin(xy[1])[2:], one_binC_common, zero_binC_common)

            i += 1
            continue

        if zero_binC_common > 0:
            xy[0] += 2 ** i
            xy[1] += 2 ** i
            # print(bin(xy[0])[2:], bin(xy[1])[2:], one_binC_common, zero_binC_common)

            zero_binC_common -= 1
        i += 1

        if one_binC_common == 0 and zero_binC_common == 0:
            break

    bin_xy = [bin(xy[i])[2:] for i in range(len(xy))]
    bin_xy_count = [bin_xy[i].count('1') for i in range(len(bin_xy))]
    max_digit = max([len(bin_xy[i])for i in range(len(bin_xy))])
    # print(bin(xy[0])[2:], bin(xy[1])[2:])
    if bin_xy_count != [a, b]:
        i = max_digit
        if a > b:
            while str(bin(xy[0])[2:]).count('1') < a:
                if bin_c[-(1 + i)] == '1':
                    xy[0] += 2 ** i
                i += 1

        else:
            while str(bin(xy[1])[2:]).count('1') < b:
                if bin_c[-(1 + i)] == '1':
                    xy[1] += 2 ** i
                i += 1

    # print(bin_c)
    # print(str(bin(xy[0])[2:]).count('1'), str(bin(xy[1])[2:]).count('1'))
    # print(bin(xy[0])[2:], bin(xy[1])[2:])
    # print([len(bin(xy[i])[2:]) for i in range(len(bin_xy))])
    if max([len(bin(xy[i])[2:]) for i in range(len(bin_xy))]) > 60:
        print(-1)
    else:
        print(xy[0], xy[1])
