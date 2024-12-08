from math import log
from functools import cache

def return_count(shou):
    count = 0
    while shou > 0:
        beki = int(log(shou, 2))
        shou -= 2 ** beki
        count += 1
    return count

s = input()
q = int(input())

k = list(map(int, input().split()))

lenS = len(s)
for index in k:
    amari = index % lenS - 1
    shou = index // lenS
    if amari == -1:
        amari = lenS - 1
        shou -= 1

    count = 0
    if shou != 0:
        while (shou != 0):
            if shou < 0:
                shou += 2 ** beki
                beki -= 1
                shou -= 2 ** beki
            beki = int(log(shou, 2))
            shou -= 2 ** beki
            count += 1

    if count % 2 == 1:
        if s[amari].isupper():
            print(s[amari].lower(), end=' ')
        else:
            print(s[amari].upper(), end=' ')
    else:
        print(s[amari], end=' ')

print()
