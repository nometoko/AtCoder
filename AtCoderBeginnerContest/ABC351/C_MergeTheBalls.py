import sys
sys.setrecursionlimit(10**9)


def MergeTheBalls(emp):
    if len(emp) <= 1 or emp[-1] != emp[-2]:
        return
    else:
        emp.pop()
        emp[-1] += 1
        return MergeTheBalls(emp)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    emp = []
    for i in range(n):
        emp.append(a[i])
        MergeTheBalls(emp)
    print(len(emp))


if __name__ == '__main__':
    main()
