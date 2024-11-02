n = int(input())
s = input()

count = 0
if len(s) >= 3:
    for i in range(n - 1):
        if s[i: i + 3] == "#.#":
            count += 1
print(count)
