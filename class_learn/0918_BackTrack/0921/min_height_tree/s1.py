import sys

sys.stdin = open("input.txt")

T = int(input())


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
    if x < y:
        parents[x] = y
    else:
        parents[y] = x


for tc in range(1, T + 1):
    # V번까지의 노드와 E개의 간선
    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        # 간선의 양 끝 노드 f, t 가중치 w
        f, t, w = map(int, input().split())
        # 정렬 편하라고 앞으로 가중치 뺌
        edge.append([w, f, t])
    edge.sort()

    parents = [i for i in range(V+1)]

    # 방문한 정점 수
    cnt = 0
    sum_weight = 0

    for w, f, t in edge:
        # 사이클이 발생하지 않는다면
        if find_set(f) != find_set(t):
            # 병합시켜줌
            union(f, t)
            cnt += 1
            sum_weight += w

            # 정점을 모두 탐색하면
            if cnt == V:
                # 탈출
                break

    print(f'#{tc} {sum_weight}')
