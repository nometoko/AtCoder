n, l = map(int, input().split())
d = list(map(int, input().split()))

pos_dict = {0: [1]}

pos = 0
ans = 0

if l % 3 != 0:
    print(ans)
    exit()

for i, di in enumerate(d):
    pos += di
    pos = pos % l

    if pos not in pos_dict:
        pos_dict[pos] = list()

    pos_dict[pos].append(i + 1)

keys = sorted(pos_dict.keys())

interval = l // 3
for key in keys:
    if key > interval:
        break
    if key + interval in pos_dict and key + 2 * interval in pos_dict:
        ans += (
            len(pos_dict[key])
            * len(pos_dict[key + interval])
            * len(pos_dict[key + 2 * interval])
        )

print(ans)
