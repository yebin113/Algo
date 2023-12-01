import sys

input = sys.stdin.readline
from collections import defaultdict


class Node:
    def __init__(self):
        # 단어의 끝을 표시하는 변수
        self.word = False
        # 자식 노드를 저장하는 딕셔너리
        self.children = {}


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root

        for char in word:
            # 자식 노드에 해당 문자가 없으면 새로운 노드 생성
            if char not in node.children:
                node.children[char] = Node()
            # 자식 노드로 이동
            node = node.children[char]
        # 동일한 이름이 있을경우에는 카운트를 세준다
        same_nick[word] += 1
        # 단어의 끝을 나타냄
        node.word = True

    def search(self, word):
        """
        주어진 단어를 검색하면서 최소 글자를 반환
        """
        node = self.root
        # 구분가능한 최소 글자를 저장
        re_word = ''
        for char in word:
            # 현재 문자를 최소 글자에 추가
            re_word += char
            # 다음 문자가 자식노드에 없으면 최소 글자 반환
            if char not in node.children:
                return re_word
            # 자식노드로 이동
            node = node.children[char]
        # 단어가 끝나면
        if node.word:
            # 카운트를 추가하고 최소 글자를 반환해준다
            re_word += str(same_nick[re_word] + 1)
        return re_word


N = int(input())
tree = Trie()
# 같은 이름의 카운트를 저장해줌
same_nick = defaultdict(int)
for _ in range(N):
    word = input().rstrip()
    print(tree.search(word))
    tree.insert(word)