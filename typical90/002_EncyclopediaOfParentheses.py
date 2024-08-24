import copy


def check(s):
    while True:
        pre_s = copy.copy(s)
        s = s.replace('()', '')
        if pre_s == s:
            break
    if s == '':
        return True
    else:
        return False


n = int(input())

left = '('
right = ')'

if n % 2 == 1:
    exit()
else:
    for i in range(2 ** n):
        s = ''
        i_bin = bin(i)[2:]
        i_bin = '0' * (n - len(i_bin)) + i_bin
        for j in i_bin:
            if j == '0':
                s += left
            else:
                s += right
        if check(s):
            print(s)
