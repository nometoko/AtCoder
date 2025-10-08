from math import log10


def add_amount(num, digit, d):
    if d != digit - (d + 1):
        return num * (10**d + 10 ** (digit - (d + 1)))
    else:
        return num * (10**d)


def base10int(value, base):
    # if int(value / base):
    #     return base10int(int(value / base), base) + str(value % base)
    # return str(value % base)
    #
    ret = ""
    while value > 0:
        ret += str(value % base)
        value //= base

    return ret[::-1]  # Reverse the string to get the correct order


def judge(num, a):
    a_ary_str = base10int(num, a)

    max_i = len(a_ary_str) // 2

    for i in range(max_i):
        if a_ary_str[i] != a_ary_str[-(i + 1)]:
            return False
    return True


def search(current_num, a, n, digit, d=0):
    ans = 0
    if current_num > n:
        raise ValueError("Current number exceeds n")

    max_d = digit // 2 if digit % 2 == 0 else digit // 2 + 1
    if d == max_d:
        if judge(current_num, a):
            return current_num
        else:
            return 0

    if d == 0:
        min_digit_num = 1
    else:
        min_digit_num = 0

    for digit_num in range(min_digit_num, 10):
        diff = add_amount(digit_num, digit, d)
        try:
            ans += search(current_num + diff, a, n, digit, d + 1)
        except ValueError:
            break

    return ans


a = int(input())
n = int(input())

n_digit = int(log10(n)) + 1

ans = 0
for digit in range(1, n_digit + 1):
    ans += search(0, a, n, digit)

print(ans)
