n = int(input())

cardList = []
for i in range(n):
    ac = list(map(int, input().split()))
    ac.append(i + 1)
    cardList.append(ac)

ans = 1
cardList.sort(reverse=True)
coat_min = cardList[0][1]
ans_list = [cardList[0][2]]
for i in range(1, n):
    if coat_min > cardList[i][1]:
        ans += 1
        ans_list.append(cardList[i][2])
        coat_min = cardList[i][1]

print(ans)
ans_list.sort()
print(*ans_list)
