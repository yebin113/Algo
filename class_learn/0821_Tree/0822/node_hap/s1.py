import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    N, M, L = map(int,input().split())
    tree = [0]*(N+1)
    #  M개의 줄에 걸쳐 리프 노드 번호와 1000이하의 자연수가 주어진다.
    for i in range(M):
        leaf, num = map(int,input().split())
        tree[leaf] = num

    c = N
    p = c // 2
    # 루트노드일때까지
    while c != 1:
        # 노드가 홀수일때 -> 왼쪽애랑 더해야함
        if c % 2 ==1 :
            tree[p] = tree[c-1] + tree[c]
            # print(c-1,'번째',tree[c-1],'더하기',c,'번째',tree[c],'는',p,'번째에 저장',tree[p],tree)
        # 노드가 짝수로 끝날때 -> 오른쪽 애랑 더해야함
        elif c%2 == 0 and c != N:
            tree[p] = tree[c] + tree[c+1]
            # print(c + 1, '번째', tree[c + 1], '더하기', c, '번째', tree[c], '는',p,'번째에 저장', tree[p], tree)

        else:
            tree[p] = tree[c]
        c -= 1
        p = c // 2
    print(f'#{tc} {tree[L]}')