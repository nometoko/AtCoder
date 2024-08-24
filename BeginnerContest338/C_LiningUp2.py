n = int(input())
q = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_max = min([q[i] // a[i] for i in range(n) if a[i] != 0])
ans_max = 0
for i in range(a_max + 1):
    q_tmp = [q[j] - (a[j] * i) for j in range(n)]
    b_max = min([q_tmp[j] // b[j] for j in range(n) if b[j] != 0])
    if i + b_max > ans_max:
        ans_max = i + b_max
print(ans_max)
