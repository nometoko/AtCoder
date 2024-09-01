s = input()
box = dict()
ind = [-1] * len(s)
depth = 0
box[0] = set()
for i in range(len(s)):
    if s[i] == '(':
        depth += 1
        box[depth] = box[depth - 1].copy()
    elif s[i] == ')':
        box.pop(depth)
        depth -= 1
    else:
        if s[i] not in box[depth]:
            box[depth].add(s[i])
        else:
            print('No')
            exit()
    # print(box)
print('Yes')
