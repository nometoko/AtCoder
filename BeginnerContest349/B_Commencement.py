s = input()
count = [0] * 100
for i in set(s):
    count[s.count(i) - 1] += 1
    s = s.replace(i, '')
    continue

for i in count:
    if i == 0 or i == 2:
        continue
    else:
        print('No')
        exit()

print('Yes')
