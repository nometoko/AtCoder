# エラトステネスの篩
n = int(input())

prime = [True] * n
prime[0] = False


maximum = int(n ** 0.5)
for i in range(2, maximum + 1):
    if prime[i - 1]:
        for j in range(i * 2, n + 1, i):
            prime[j - 1] = False

for i in range(len(prime)):
    if prime[i]:
        print(i + 1)
