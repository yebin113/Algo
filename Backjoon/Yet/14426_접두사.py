class Node(object):
    def __init__(self, key, data=None):
        """
        :param key: 값으로 입력될 문자
        :param data: 문자열 종료를 알림
        :param children: 자식 노드
        """
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        """
        루트를 빈 노드로 설정함
        """
        self.head = Node(None)

    def insert(self, string):
        """
        트리를 생성하기 위한 함수
        입력된 문자열의 문자를 하나씩 children에 확인 후 저장하고
        문자열을 다 돌면 마지막 노드의 data에 문자열을 저장
        """
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string


    def search(self, string):
        """
        문자열이 존재하는지에 대한 여부를 리턴
        문자열을 하나씩 돌면서 확인 후 마지막 노드가 data가 존재한다면 True
        그렇지 않음 False 리턴
        """
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        # 문자열이 자기 자신이거나 접두사일때 True
        if current_node.data or current_node.children:
            return True
        else:
            return False


trie = Trie()


n, m = map(int, input().split())

for i in range(n):
    # 트리에 삽입
    word = input()

    trie.insert(word)
# print(Node)
cnt = 0
for i in range(m):
    # 트리에서 찾기
    prefix = input()
    if trie.search(prefix):
        cnt += 1
print(cnt)
















