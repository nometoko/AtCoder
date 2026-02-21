n = int(input())
a = list(map(int, input().split()))

a_max = max(a)
arr = [0] * (a_max)

for val in a:
    arr[val - 1] += 1

for i in range(a_max - 1, 0, -1):
    arr[i - 1] += arr[i]

answer = ""
motikoshi = 0
for val in arr:
    val += motikoshi
    answer = str(val % 10) + answer
    motikoshi = val // 10

if motikoshi > 0:
    answer = str(motikoshi) + answer
print(answer)
