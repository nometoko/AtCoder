n, w = map(int, input().split())

block_by_column = [[] for _ in range(w)]
delete_time_list = [-1] * n

for i in range(n):
    x, y = map(int, input().split())
    block_by_column[x - 1].append([y, i])

for y_list in block_by_column:
    y_list.sort()

delete_row_num = min([len(column) for column in block_by_column])

for i in range(delete_row_num):
    delete_time = max([block_by_column[column][i][0] for column in range(w)])
    for column in range(w):
        block_ind = block_by_column[column][i][1]
        delete_time_list[block_ind] = delete_time

q = int(input())

for _ in range(q):
    t, a = map(int, input().split())
    delete_time_a = delete_time_list[a - 1]
    if delete_time_a == -1 or delete_time_a > t:
        print("Yes")
    else:
        print("No")
