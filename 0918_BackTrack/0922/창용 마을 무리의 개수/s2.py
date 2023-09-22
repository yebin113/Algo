import sys

sys.stdin = open("input.txt")

def find_set(x):
    if parents[x] == x:
        return x
    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    # 사이클발생
    if x == y:
        return
    # 통합시켜주기
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


T = int(input())

for tc in range(1, T + 1):
    # 창용 마을에 사는 사람의 수와 서로를 알고 있는 사람의 관계 수(노드와 간선)
    N, M = map(int, input().split())
    parents = [i for i in range(N)]
    # 인접 리스트
    arr = [[] for _ in range(N)]
    # M개의 줄에 걸쳐서 서로를 알고 있는 두 사람의 번호
    for i in range(M):
        n1, n2 = map(int, input().split())
        # 무방향
        arr[n1 - 1].append(n2 - 1)
        arr[n2 - 1].append(n1 - 1)
        union(n1-1,n2-1)


    for i in range(N):
        if parents[i] != i:
            find_set(i)

    res = list(set(parents))
    print(f'#{tc} {len(res)}')
