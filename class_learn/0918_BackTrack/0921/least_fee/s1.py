import sys

sys.stdin = open("input.txt")

T = int(input())


def find_set(x):
    if parents[x] == x:
        return

    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


dxy = [ [1, 0], [0, 1]]
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    parents = [i for i in range(N * N)]
    edge = []
    for i in range(N):
        for j in range(N):
            for di, dj in dxy:
                ni = i + di
                nj = j + dj

                if 0 <= ni < N and 0 <= nj < N:
                    # 가중치
                    w = abs(arr[i][j] - arr[ni][nj]) + 1
                    # 일차원으로 바꿔줌
                    f = N * i + j
                    t = N * ni + nj
                    edge.append([w, f, t])
    edge.sort()
    print(edge)
    # 들르는 정점의 수를 카운트
    cnt = 0
    # 가중치 누적합
    sum_weight = 0
    for w, f, t in edge:
        # 사이클이 아니라면
        if find_set(f) != find_set(t):
            # 병합시켜준다
            union(f, t)
            cnt += 1
            sum_weight += w

        if cnt == N * N:
            break
    print(parents)
    print(f'#{tc} {sum_weight}')
