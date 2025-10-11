s = input()

num = 0
index = [-1, -1]

for i, char in enumerate(s):
    if char == "#":
        num += 1
        index[1 - (num % 2)] = i + 1
        if num > 0 and num % 2 == 0:
            print(index[0], index[1], sep=",")
