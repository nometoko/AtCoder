def back(left, right, i, point):
    point.append(right)
    while left != right:
        right -= 2 ** i
        if left > right:
            right += 2 ** i
        else:
            point.append(right)
        i -= 1
    return sorted(list(set(point)))


def forward(left, right, i, point):
    point.append(left)
    while left != right:
        # print(left, right)
        left += 2 ** i
        if left > right:
            left -= 2 ** i
        else:
            point.append(left)
        i -= 1
    return sorted(list(set(point)))


def main():
    left, right = map(int, input().split())
    point = [left, right]
    i = 0
    while 2 ** i <= right - left:
        i += 1
    i -= 1
    j = (2 ** i) * (left // (2 ** i) + 1)

    point = back(left, j, i, point)
    point = forward(j, right, i, point)
    print(len(point) - 1)
    for i in range(len(point) - 1):
        print(point[i], point[i + 1])


if __name__ == '__main__':
    main()
