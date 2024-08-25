from functools import lru_cache

n = int(input())
@lru_cache(maxsize=1000)
def kansuu(a):
    if a>0:
        return a*kansuu(a-1)
    else:
        return 1
print(kansuu(n))