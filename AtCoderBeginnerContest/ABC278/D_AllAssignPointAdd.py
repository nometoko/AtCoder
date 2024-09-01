n = int(input())
a = list(map(int, input().split()))
q = int(input())

diff = dict()
all = -1
for i in range(n):
    diff[i] = a[i]

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        diff = dict()
        all = query[1]
    elif query[0] == 2:
        if query[1] - 1 in diff:
            diff[query[1] - 1] += query[2]
        else:
            diff[query[1] - 1] = query[2]
    else:
        if all == -1:
            print(diff[query[1] - 1])
        else:
            if query[1] - 1 in diff:
                print(diff[query[1] - 1] + all)
            else:
                print(all)
