def binarySearch(target, arr, n):
    index = n // 2
    division = 2
    while not arr[index] < target <= arr[index + 1]:
        # print(index, arr[index], target)
        division *= 2
        if arr[index] < target:
            index += n // division + 1
        else:
            index -= n // division + 1
        if index >= n:
            index = n - 1
        elif index < 0:
            index = 0
        # もう一つの終了条件
        if index == 0 and target < arr[index]:
            index = -1
            break
        if index == n - 1 and target > arr[index]:
            break
    while index < n - 1 and arr[index] == arr[index + 1]:
        index += 1
    return index


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    q = int(input())
    for _ in range(q):
        x = int(input())
        index = binarySearch(x, a, n)
        print(index + 1)


if __name__ == '__main__':
    main()
