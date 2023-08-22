

import sys
sys.stdin = open("input.txt")


def enq(item):
    """
    enq(item)
    현재 위치의 부모랑 비교.
    부모보다 부모가 더 크면 자리를 바꿈
    현재 위치에서 또 비교
    정렬될때까지 반복
    """
    global rear
    rear += 1
    heap[rear] = item

    c = rear
    p = rear//2
    while c != 1:    # 자식노드가 루트노드가 아닐때까지
        if heap[c] < heap[p]:   # 만약 자식노드가 부모 노드보다 작다면
            heap[c],heap[p] = heap[p],heap[c]   # 자리를 바꿈
            c = p   # 부모노드로 올라가기
            p = c//2
        else:
            break


def deq():
    global last
    tmp = heap[1]       # 루트 백업
    heap[1] = heap[last]    # 마지막 노드값을 루트에 가져다 놓음
    last -= 1               # 마지막 노드 삭제
    p = 1           # 루트에 옮긴 값을 자식과 비교
    c = p * 2       # 왼쪽 자식(비교할 자식노드 번호)
    while c <= last:        # 자식이 하나라도 있으면
        if c + 1 <= last and heap[c] < heap[c+1]:        # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1      # 오른쪽 자식과 비교하기 위해 비교할 자식노드 번호를 1 추가
        if heap[p] < heap[c]:       # 자식이 더 크면 최대힙 규칙에 어긋나므로
            heap[p] , heap[c] = heap[c], heap[p]
            p = c   # 자식을 새로운 부모로
            c = p * 2        # 왼쪽 자식 번호를 계산
        else:       # 부모가 더 크면
            break   # 탈출
            
    return tmp


def hap(c):
    """
    현재 위치의 노드가 주어졌을때, 그 조상들의 합을 구하는 함수
    일단 주어진 위치의 부모를 더한다
    그리고 자식노드의 위치를 부모 노드로 바꿔주고
    부모노드의 위치는 현재 자식 노드의 //2 로 바꿔준다
    자식노드가 1이 될때 까지 반복한다
    """
    parent_hap = 0
    p = c // 2

    while c != 1:
        parent_hap += heap[p]
        c = p
        p = c // 2
    return parent_hap


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    rear = 0
    heap = [0] * (N+1)
    last = 0
    for i in range(N):
        enq(arr[i])


    print(heap)
    print(f'#{tc} {hap(N)}')  # 번수랑 인덱스랑 헷갈리지 말긔..
