import sys
sys.stdin = open("input.txt")

T = int(input())

def inorder(n):
    global root

    if n > N:
        return
    inorder(2*n)
    tree[n] = root
    root += 1
    inorder(2*n + 1)

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    tree = [0] * (N+1)  # 입력받은 완전 이진트리를 저장 , 1번 인덱스부터 사용한다
    # 0번 인덱스를 사용하지 않는다
    for i in range(1,N+1):
        tree[i] = arr[i-1]
        # i 가 1보다 크다면, 부모 노드가 있다는 것
        # 부모 노드와 비교 후, 이진 최소힙 구성 조건에 맞게 swap할지 결정
        while i >= 2:
            # 부모 노드의 인덱스
            parent = i // 2
            # 부모 노드의 값이 더 크다면 swap
            if tree[i] <= tree[parent]:
                tree[i],tree[parent] = tree[parent],tree[i]
            i = N//2        # 부모 노드의 위치
        result = 0
        while N!= 0:
            N = N//2        # 부모 노드의 위치를 구하기
            result += tree[N]
        print(tree)

    print(f'#{tc} {result}')
