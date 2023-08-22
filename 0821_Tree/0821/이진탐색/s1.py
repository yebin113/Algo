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
    tree = [0] * (N+1)  # N번 노드까지  있는 완전 이진 트리
    root = 1
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')
