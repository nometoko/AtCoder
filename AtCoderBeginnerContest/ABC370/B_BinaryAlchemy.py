n = int(input())

a = []
for i in range(n):
    a_tmp = list(map(int, input().split()))
    a_tmp = [tmp - 1 for tmp in a_tmp]
    a.append(a_tmp)

now = 0
for i in range(n):
    now = a[max(now, i)][min(now, i)]

print(now + 1)
