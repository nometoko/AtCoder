import math

def main():
    n, m, k = map(int, input().split())
    gcd = math.gcd(n, m)
    lcm = math.lcm(n, m)
    cycle = lcm // n + lcm // m - 2
    ans = ((k - 1) // cycle) * lcm
    amari = (k - 1) % cycle + 1
    a = n
    b = m
    for _ in range(1, amari):
        if a < b:
            a += n
        else:
            b += m
    ans += min(a, b)
    print(ans)


if __name__ == '__main__':
    main()
