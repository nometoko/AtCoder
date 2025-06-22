n = int(input())
t = input()
a = input()

for t_i, a_i in zip(t, a):
    if t_i == "o" and a_i == "o":
        print("Yes")
        exit()

print("No")
