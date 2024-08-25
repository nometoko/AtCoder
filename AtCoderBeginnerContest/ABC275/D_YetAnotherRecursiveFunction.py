def kansuu(A):
    if A == 0:
        return 1
    else:
        a = kansuu(A//2)
        b = kansuu(A//3)
        return a+b

n = int(input())
print(kansuu(n))