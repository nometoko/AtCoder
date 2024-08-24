import bisect


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    sortSetA = sorted(list(set(a)))
    for i in range(n):
        b[i] = bisect.bisect_left(sortSetA, a[i]) + 1
    print(*b)


if __name__ == '__main__':
    main()
