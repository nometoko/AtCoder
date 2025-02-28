from collections import deque
s = input()

pair = ['()', '[]', '<>']
waiting = deque()
for i, c in enumerate(s):
    ch = waiting.pop() if waiting else None
    if ch is None:
        waiting.append(c)
        continue
    elif ch + c in pair:
        continue
    else:
        waiting.append(ch)
        waiting.append(c)

if waiting:
    print('No')
else:
    print('Yes')
