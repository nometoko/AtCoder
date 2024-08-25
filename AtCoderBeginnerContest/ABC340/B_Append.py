q = int(input())
query = []
for _ in range(q):
    command, value = map(int, input().split())
    if command == 1:
        query.append(value)
    else:
        print(query[-value])
