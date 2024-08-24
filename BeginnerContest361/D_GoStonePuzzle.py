# https://atcoder.jp/contests/abc361/tasks/abc361_d

import collections

def move(string, index):
    string_list = list(string)
    dotIndex = string.index('.')
    tmp = string_list[index: index + 2]
    string_list[index: index + 2] = ['.', '.']
    string_list[dotIndex: dotIndex + 2] = tmp
    return ''.join(string_list)


if __name__ == '__main__':
    n = int(input())
    s = input()
    t = input()

    s = s + '..'
    t = t + '..'

    searched = set()
    will_search = collections.deque()
    will_search.append([s, 0])
    if s.count('W') != t.count('W'):
        print(-1)
        exit()
    
    while will_search:
        s, depth = will_search.popleft()
        # print(s, depth)
        if s == t:
            print(depth)
            exit()
        if s in searched:
            continue
        searched.add(s)
        for i in range(n + 1):
            if s[i] != '.' and s[i + 1] != '.':
                new_s = move(s, i)
                if new_s not in searched:
                    will_search.append([new_s, depth + 1])
    
    print(-1)
