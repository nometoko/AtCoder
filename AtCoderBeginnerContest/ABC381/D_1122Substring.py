def return_ans(a):
    start_ind = 0
    end_ind = 1
    num_list = set()
    ans = 0
    n = len(a)
    while end_ind < n:

        if a[end_ind] == a[end_ind - 1]:
            if a[end_ind] not in num_list:
                num_list.add(a[end_ind])
                ans = max(ans, end_ind - start_ind + 1)
                end_ind += 2

            else:
                num_list.remove(a[start_ind])
                start_ind += 2
                if start_ind > end_ind:
                    exit(-1)

        else:
            num_list = set()
            start_ind = end_ind + 1
            end_ind += 2
    return ans


n = int(input())
a = list(map(int, input().split()))

ans = max(0, return_ans(a), return_ans(a[1:]))
print(ans)
