n = int(input())
a = list(map(int, input().split()))
sortList = [[a[i], i] for i in range(n)]
sortList.sort(reverse=True)
print(sortList[1][1] + 1)
