n, q = map(int, input().split())

versions = [1] * n
min_version = 1
for _ in range(q):
    x, y = map(int, input().split())
    if x < min_version:
        print(0)
        continue

    cnt = 0
    for version in range(min_version, x + 1):
        cnt += versions[version - 1]
        versions[version - 1] = 0

    versions[y - 1] += cnt
    min_version = x + 1
    print(cnt)
