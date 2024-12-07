n = int(input())

maxValue = int(pow(n, 0.5))

def eratosthenes2(n):
    primeList = []
    if n < 2:
        return primeList
    is_prime = ([False, True] * (n // 2 + 1))[0: n + 1]
    is_prime[1] = False
    is_prime[2] = True
    primeList.append(2)
    i = 3
    for i in range(3, n + 1, 2):
        if not(is_prime[i]):
            continue
        primeList.append(i)
        if i * i > n:
            break
        for k in range(i * i, n + 1, i):
            is_prime[k] = False

    for i in range(i + 2, n + 1, 2):
        if is_prime[i]:
            primeList.append(i)
    return primeList


primeList = eratosthenes2(maxValue)
count = 0
for i, primeFirst in enumerate(primeList):
    # 二分探索
    left = 0
    right = len(primeList)
    while left < right:
        mid = (left + right) // 2
        if primeFirst * primeList[mid] <= maxValue:
            left = mid + 1
        else:
            right = mid
    if left - 1 > i:
        # print(primeFirst, primeFirst * primeList[left - 1], primeFirst * primeList[left])
        count += left - i - 1
    else:
        break

for prime in primeList:
    if pow(prime, 4) <= maxValue:
        count += 1

print(count)
