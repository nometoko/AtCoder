from collections import deque


class Node:
    def __init__(self, word, pare):
        self.word = word
        self.pare = pare
        self.cnt = 0
        self.child = dict()

    def add_child(self, child_word):
        child = Node(child_word, self)
        self.child[child_word] = child

    def add_cnt(self):
        self.cnt += 1


class Trie:
    def __init__(self):
        self.root = Node("", None)
        self.cnt = 0

    def search(self, word):
        node = self.root
        for i in range(len(word)):
            if word[:i] in node.child:
                node = node.child[word[:i]]
            else:
                return False

        return True

    def add(self, word):
        node = self.root
        for char in word:
            if char not in node.child:
                node.add_child(char)

            node = node.child[char]
            node.add_cnt()
            if node.cnt > 1:
                self.cnt += node.cnt - 1

    # def count(self):
    #     q = deque([self.root])
    #
    #     cnt = 0
    #     while q:
    #         node = q.popleft()
    #
    #         cnt += (node.cnt * (node.cnt - 1)) // 2
    #
    #         for child in node.child:
    #             q.append(node.child[child])
    #
    #     return cnt


def main():
    n = int(input())
    s = input().split()
    trie = Trie()

    for word in s:
        trie.add(word)

    print(trie.cnt)
    return


if __name__ == "__main__":
    main()
