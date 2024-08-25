import itertools


def tiling(tile_list, tileMap, depth):
    # print(tile_list)

    tmpMap = [i.copy() for i in tileMap]
    isBreak = False
    lossList = []
    i, j = 0, 0
    for i in range(len(tileMap)):
        for j in range(len(tileMap[0])):
            if tileMap[i][j] == 0:
                isBreak = True
                break
        if isBreak:
            break
    # ---end--- #
    if isBreak is False:
        return True

    if len(tile_list) == 0:
        return False
    for num in range(len(tile_list)):
        if tile_list[num] in lossList:
            continue
        # tMap = [[i.copy() for i in tmpMap] for _ in range(2)]
        isBreak = False
        for k, l in itertools.product(range(tile_list[0]), range(tile_list[1])):
            try:
                if tileMap[i + l][j + k] == 0:
                    tileMap[i + l][j + k] = 1
                    continue
                else:
                    isBreak = True
                    break
            except IndexError:
                isBreak = True
                break
        if isBreak is False:
            # print('put a tile', tile_list[num])
            # for mapp in tileMap:
            #     print(mapp)
            if tiling(tile_list[0:num] + tile_list[num + 1:], tileMap, depth + 1):
                return True

        tileMap = [i.copy() for i in tmpMap]
        isBreak = False
        for k, l in itertools.product(range(tile_list[0]), range(tile_list[1])):
            try:
                if tileMap[i + k][j + l] == 0:
                    tileMap[i + k][j + l] = 1
                    continue
                else:
                    isBreak = True
                    break
            except IndexError:
                isBreak = True
                break

        if isBreak is False:
            # print('put a tile', tile_list[num])
            # for mapp in tileMap:
            #     print(mapp)
            if tiling(tile_list[0:num] + tile_list[num + 1:], tileMap, depth + 1):
                return True
        tileMap = [i.copy() for i in tmpMap]
        lossList.append(tile_list[num])
    return False


def main():
    n, h, w = map(int, input().split())
    tileList = []
    for i in range(n):
        tileList.append(list(map(int, input().split())))
    tileMap = [[0] * w for _ in range(h)]
    if tiling(tileList, tileMap, 1):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
