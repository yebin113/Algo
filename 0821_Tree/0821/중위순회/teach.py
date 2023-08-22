import sys
sys.stdin = open("input.txt")

# 전위순회
def preorder(p,N):   # N 완전 이진트리의 마지막 정점
    if p <= N:
        print(tree[p], end='')
        inorder(p*2,N)
        inorder(p*2+1,N)

# 중위 순회
def inorder(p,N):   # N 완전 이진트리의 마지막 정점
    if p <= N:
        inorder(p*2,N)
        print(tree[p], end='')
        inorder(p*2+1,N)


T = 10
for tc in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1)  # N번 노드까지  있는 완전 이진 트리
    for _ in range(N):
        arr = list(input().split())
        tree[int(arr[0])] = arr[1]
    print(f'#{tc}', end = ' ')
    inorder(1,N)
    print()
