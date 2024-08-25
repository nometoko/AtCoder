from functools import cache
div = 998244353


@cache
def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1
    K = 1
    while n > 1:
        if n % 2 != 0:
            K = (K * x) % div
            x = (x ** 2) % div
            n = (n - 1) // 2
        else:
            x = x ** 2 % div
            n = n // 2
    return (K * x) % div  # 指数を割り続け n が 1 に至ったら終了


n = int(input())
length = len(str(n))
r = 10 ** length % div
ans = (n % div) * (pow_k(r, n) - 1) * pow_k((r - 1) % div, div - 2)
print(ans % div)
