import itertools
from numpy import cbrt
from math import sqrt

def primeFactorization(n):
    res = []
    ex = 0
    while n % 2 == 0:
        n //= 2
        ex += 1
    if ex > 0:
        res.append((2, ex))

    for i in range(3, int(n**0.5)+1, 2):
        if n % i != 0:
            continue
        ex = 0
        while n % i == 0:
            ex += 1
            n //= i
        res.append((i, ex))
    if n != 1:
        res.append((n, 1))
    return res

n = int(input())
factors = primeFactorization(n)
allFactors = []
for factor, ex in factors:
    for i in range(1, ex + 1):
        allFactors.append(factor ** i)
factorsSum = len(allFactors)

divisors = set([1])
for i in range(1, factorsSum + 1):
    for comb in itertools.combinations(allFactors, i):
        divisor = 1
        for num in comb:
            divisor *= num
        divisors.add(divisor)

divisors.add(n)
# print(divisors)

lenDivisors = len(divisors)
divisors = sorted(list(divisors))

for divisor in divisors:
    # print(divisor)
    other = n // divisor
    xMax = int(sqrt(other)) + 1
    xMin = max(2, divisor)

    while xMin <= xMax:
        x = (xMin + xMax) // 2
        y = x - divisor
        # print(f'\t{x}, \t{y}')
        if x ** 3 - y ** 3 == n:
            print(x, y)
            exit()
        elif x ** 3 - y ** 3 < n:
            xMin = x + 1
        else:
            xMax = x - 1

print(-1)
