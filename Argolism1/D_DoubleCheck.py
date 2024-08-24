import collections

n = int(input())
num = []
a = []
for i in range(n):
    a.append(int(input()))
    num.append(i + 1)

a_sorted = sorted(a)

items_list_collection = collections.Counter(a)
# リスト内包表記で、個数が2個以上のキーを要素として取り込む
new_items_list = [k for k, v in items_list_collection.items() if v > 1]
try:
    print(new_items_list[0], end=' ')
    print(list(set(num) - set(a_sorted))[0])

except IndexError:
    print('Correct')
