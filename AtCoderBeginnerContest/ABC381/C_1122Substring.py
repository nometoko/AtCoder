import re

n = int(input())

s = input()

ans = 1

sla_ind = [m.start() for m in re.finditer("/", s)]

for ind in sla_ind:
    search = 1
    # print(f"search for ind {ind}")
    while search <= ind and search + ind < n:
        # print("\t", s[ind - search], s[ind + search])
        if s[ind - search] != "1" or s[ind + search] != "2":
            break
        search += 1
    # print(ind, search)
    ans = max(ans, search * 2 - 1)

print(ans)
