"""
깊은 딕셔너리 구조로 간이 트리 만들기
사전순서로 키를 정렬한 뒤, 값이 존재하면 --를 붙이고 출력하기
"""


N = int(input())
tri = dict()
for _ in range(N):
    # 딕셔너리의 key와 value 로 트리 형식의 데이터 구조 만듬
    prey_info = list(input().split())
    info = tri
    for i in range(1,len(prey_info)):
        if prey_info[i] not in info:
            info[prey_info[i]] = dict()
        info = info[prey_info[i]]
# print(tri)

def print_tree(trie, depth=0):
    """
    재귀형식으로 다음 value를 key에서 찾아서 가지를 찾아가는 구조

    :param trie: 주어진 딕셔너리
    :param depth: 들어온 깊이
    :return: 없음 현재의 key를 출력함
    """

    # 정렬한 키를 순회하면서
    for key in sorted(trie.keys()):
        # 키를 들어온 만큼 --를 출력한 뒤 키를 출력함
        print('--' * depth + key)
        next_key = trie[key]
        # 객체의 타입을 확인함
        # 지금 키의 값이 존재하는지 안하는지 확인하기 위해 사용됨
        if isinstance(next_key, dict):
            # 다음 키의 value 가 존재한다면 재귀
            print_tree(next_key, depth + 1)

print_tree(tri)

