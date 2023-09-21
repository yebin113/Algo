import sys

sys.stdin = open('input.txt')

T = int(input())


def bfs(i, j):
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    q = [(i, j)]

    while q:
        i, j = q.pop(0)
        for di, dj in dxy:
            # 델타 탐색
            ni = i + di
            nj = j + dj
            # 범위 안에 있는 인덱스이고, 방문하지 않은 곳이라면
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                # 큐에 추가
                q.append((ni, nj))
                # 만약 다음 곳이 더 높을때
                if arr[i][j] < arr[ni][nj]:
                    # 그 차 만큼 연료가 더 든다
                    visited[ni][nj] += arr[ni][nj] - arr[i][j]
                # 그리고 기존 누적값에 연료 기본으로 1 들어감
                visited[ni][nj] += visited[i][j] + 1
            # 벽 안에 있는데 방문했던 곳이면
            elif 0 <= ni < N and 0 <= nj < N:
                # 더 적은 연료로 갈수있는걸로 교체!
                if arr[i][j] < arr[ni][nj]:
                    # 다음이 더 높다면, 지금 방문값 vs 누적값 + 기본 연료 1 + 높이의 차
                    visited[ni][nj] = min(visited[ni][nj], visited[i][j] + arr[ni][nj] - arr[i][j] + 1)
                else:
                    # 다음이 높지 않다면, 지금 방문값 vs 누적값 + 1
                    visited[ni][nj] = min(visited[ni][nj], visited[i][j] + 1)
    # 맨 마지막 값을 반환
    return visited[-1][-1]-1

dxy = [[1, 0], [0, 1],[-1,0],[0,-1]]
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    bfs(0, 0)
    print(f'#{tc} {bfs(0, 0)}')
