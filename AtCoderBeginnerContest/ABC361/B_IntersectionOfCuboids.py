cube1 = list(map(int, input().split()))
cube2 = list(map(int, input().split()))

for i in range(3):
    if cube1[i] <= cube2[i] < cube1[i + 3] or cube1[i] < cube2[i + 3] <= cube1[i + 3] or (cube2[i] <= cube1[i] and cube2[i + 3] >= cube1[i + 3]):
        continue
    else:
        print("No")
        exit()
print("Yes")
