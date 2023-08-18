import sys

sys.stdin = open("input.txt")


def bfs(sti, stj, N):
    # visited는 미로와 동일한 배열로 작성
    visited = [[0] * N for _ in range(N)]
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append((sti, stj))
    # 시작점 인큐표시
    visited[sti][stj] = 1
    # 큐가 비워질 때까지
    while q:
        # deq
        i, j = q.pop(0)  # 0빼먹으면 dfs 됨
        if arr[i][j] == 3:  # 목적지 확인
            return visited[i][j] - 2  # 지나온 칸수 리턴
        # 인접하고 인큐된 적이 없으면
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            # 범위 벽세우기, 1인 벽이 아니고 방문한 곳이 아닐때
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    return 0  # 3인 도착지에 도착 못할때 0을 리턴


def find_start(N):
    # 시작점을 찾음
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for i in range(N)]

    # 시작점을 찾음
    sti, stj = find_start(N)
    print(sti,stj)

    ans = bfs(sti, stj, N)

    print(f'#{tc} {ans}')
