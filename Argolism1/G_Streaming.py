import itertools


def return_max_index(array):
    tmp_array = [tmp.copy() for tmp in array]
    index = [0] * 2
    max_list = [max(i) for i in tmp_array]
    maximum_value = max(max_list)
    index[0] = max_list.index(maximum_value)
    index[1] = tmp_array[index[0]].index(maximum_value)
    return index, tmp_array


def calc_happiness(streaming_array, happiness_table):
    happiness = 0
    for i in streaming_array:
        if len(i) == 1:
            continue
        else:
            comb = list(itertools.combinations(i, 2))
            for j in comb:
                happiness += happiness_table[j[0] - 1][j[1] - j[0] - 1]
            continue
    return happiness


def main():
    # initialize
    n = int(input())
    a = []
    streaming_array = []

    for i in range(n - 1):
        a.append(list(map(int, input().split())))
        streaming_array.append([i + 1])
    streaming_array.append([n])
    tmp_array = a

    while True:
        index, tmp_array = return_max_index(tmp_array)
        tmp_streaming = [tmp.copy() for tmp in streaming_array]
        if tmp_array[index[0]][index[1]] <= 0:
            break
        tmp_array[index[0]][index[1]] = 0

        first_person = index[0] + 1
        second_person = index[1] + first_person + 1

        is_break = False
        for i in range(len(tmp_streaming)):
            if first_person in tmp_streaming[i]:
                for j in range(len(tmp_streaming)):
                    if second_person in tmp_streaming[j]:
                        tmp_streaming[i].extend(tmp_streaming[j])
                        tmp_streaming.remove(tmp_streaming[j])
                        is_break = True
                        break
            if is_break:
                break
        if calc_happiness(streaming_array, a) < calc_happiness(tmp_streaming, a):
            streaming_array = tmp_streaming

    print(calc_happiness(streaming_array, a))


if __name__ == "__main__":
    main()
