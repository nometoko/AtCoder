"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""


def factorization(n):
    arr = []
    tmp = n
    cnt = 0
    if tmp % 2 == 0:
        while tmp % 2 == 0:
            tmp //= 2
            cnt += 1
        arr.append([2, cnt])

    for i in range(3, int(-(-n ** 0.5 // 1)) + 1, 2):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])

    if tmp != 1:
        arr.append([tmp, 1])

    if not arr:
        arr.append([n, 1])

    return arr


def main():
    k = int(input())
    arr = factorization(k)
    ans = []
    # print(arr)
    for i in arr:
        tmp = 0
        while i[1] > 0:
            tmp += i[0]
            tmptmp = tmp
            while tmptmp % i[0] == 0:
                tmptmp /= i[0]
                i[1] -= 1
        ans.append(tmp)
    print(max(ans))


if __name__ == '__main__':
    main()