def PrimeCheck(num):
    if num == 2:
        print('Yes')
        return

    if num == 1 or num % 2 == 0:
        print('No')
        return
    else:
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                print('No')
                return
        print('Yes')
        return


q = (int(input()))

for i in range(q):
    x = int(input())
    PrimeCheck(x)
