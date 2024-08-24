n = int(input())
userList = []
rateSum = 0
for _ in range(n):
    name, rate = input().split()
    userList.append(name)
    rateSum += int(rate)

userList.sort()
print(userList[rateSum % n])
