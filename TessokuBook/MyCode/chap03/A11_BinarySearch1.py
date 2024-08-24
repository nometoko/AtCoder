def binarySearch(target, arr, n):
    index = n // 2
    division = 2
    while arr[index] != target:
        division *= 2
        if arr[index] < target:
            index += n // division + 1
        else:
            index -= n // division + 1
        if index >= n:
            index = n - 1
        elif index < 0:
            index = 0
    return index


def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    index = binarySearch(a, n, x)
    print(index + 1)

if __name__ == '__main__':
    main()
