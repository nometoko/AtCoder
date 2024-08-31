import numpy as np
s = []
pos = []
for i in range(9):
    tmp = list(input())
    s.append(tmp)
    for j in range(9):
        if tmp[j] == '#':
            pos.append((i, j))

ans = 0
len_pos = len(pos)
for i in range(len_pos):
    pos1 = np.array(pos[i])
    for j in range(i + 1, len_pos):
        pos2 = np.array(pos[j])
        vec = pos2 - pos1
        vec = np.array([- vec[1], vec[0]])
        pos3 = pos2 + vec
        if (0 <= pos3[0] < 9 and 0 <= pos3[1] < 9) and s[pos3[0]][pos3[1]] == '#':
            if (pos3[0] < pos1[0] and pos3[1] < pos1[1]) or (pos3[0] < pos2[0] and pos3[1] < pos2[1]):
                continue
            vec = np.array([- vec[1], vec[0]])
            pos4 = pos3 + vec
            if (0 <= pos4[0] < 9 and 0 <= pos4[1] < 9) and s[pos4[0]][pos4[1]] == '#':
                if (pos4[0] < pos1[0] and pos4[1] < pos1[1]) or (pos4[0] < pos2[0] and pos4[1] < pos2[1]) or (pos4[0] < pos3[0] and pos4[1] < pos3[1]):
                    continue
                # print(pos1, pos2, pos3, pos4)
                ans += 1
print(ans)
