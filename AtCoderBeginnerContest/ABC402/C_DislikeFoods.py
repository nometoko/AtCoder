n, m = map(int, input().split())

dishes = [set() for _ in range(n)]
ingredients_num = [0] * m

# 料理のfor loop
for i in range(m):
    ingredients = list(map(int, input().split()))
    for ingredient in ingredients[1:]:
        dishes[ingredient - 1].add(i + 1)
        ingredients_num[i] += 1

overcome = list(map(int, input().split()))

ans = 0
for food in overcome:
    dish = dishes[food - 1]
    for ingredient in dish:
        ingredients_num[ingredient - 1] -= 1
        if ingredients_num[ingredient - 1] == 0:
            ans += 1


    print(ans)
