import sys
sys.stdin = open("input.txt")

T = 10
word_list = []

"""
def inorder_traverse (T) :  # 중위순회
  if T:                     # T is not None
    inorder traverse(T.left)
    visit (T)               # print(T.item)
    inorder_traverse (T.right)
"""
def in_order(start):
    # 두 노드가 있을때
    if ch1[start] != 0 and ch2[start]:
        # 왼쪽을 가장 먼저 탐색
        in_order(ch1[start])
        # 그다음 부모
        print(word_dict[start],end='')
        # 그 다음 오른쪽
        in_order(ch2[start])
    elif ch1[start] != 0:
        in_order(ch1[start])
        print(word_dict[start], end='')
    else:
        print(word_dict[start], end='')





for tc in range(1, T+1):
    # 정점의 총 수
    N = int(input())
    word_dict = {}
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)
    for i in range(N):
        arr = list(map(str, input().split()))
        # 해당 정점
        number = int(arr.pop(0))
        # 정점의 글자
        word = arr.pop(0)
        # 쉽게 변환하기 위해 딕셔너리에 대응
        word_dict[number] = word
        # 부모 인덱스에 자식 저장
        if len(arr) == 2:
            ch1[number] = int(arr[0])
            ch2[number] = int(arr[1])
        elif len(arr) == 1:
            ch1[number] = int(arr[0])


    print(f'#{tc}',end=' ')
    in_order(1)
    print()
