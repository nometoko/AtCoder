rookMap = [input() for _ in range(8)]

row = [False] * 8
col = [False] * 8
for i in range(8):
    for j in range(8):
        if rookMap[i][j] == '#':
            row[i] = True
            col[j] = True

count = 0
for i in range(8):
    for j in range(8):
        if row[i] == False and col[j] == False:
            count += 1
    
print(count)
