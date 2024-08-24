def gcd(a, b):
    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b
    return b


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == '__main__':
    main()
