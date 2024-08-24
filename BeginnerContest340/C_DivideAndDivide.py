from functools import cache


# メモ化
@cache
def DivideAndDivide(num):
    # print(num)
    if num < 2:
        return 0

    if num % 2 == 1:
        return num + DivideAndDivide(num // 2) + DivideAndDivide(num // 2 + 1)
    else:
        return num + (DivideAndDivide(num // 2) * 2)


def main():
    n = int(input())
    print(DivideAndDivide(n))


if __name__ == '__main__':
    main()
