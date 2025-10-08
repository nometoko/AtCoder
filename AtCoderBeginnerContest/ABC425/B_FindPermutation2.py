n = int(input())
a = list(map(int, input().split()))

num_set = set([i for i in range(1, n + 1)])
for num in range(1, n + 1):
    num_cnt = a.count(num)
    if num_cnt > 1:
        print("No")
        exit()
    elif num_cnt == 1:
        num_set.remove(num)

print("Yes")

for val in a:
    if val == -1:
        print(num_set.pop(), end=" ")
    else:
        print(val, end=" ")
print()
