import sys
from collections import deque


def bfs(arr, start_list):
    # print(start_list)
    is_spread = True
    visited = [[0] * N for _ in range(N)]
    day = 0
    q = start_list
    # 시작점 방문 체크
    for m in range(M):
        i, j = start_list[m]
        visited[i][j] = 1
    while q:
        i, j = q.popleft()
        for di, dj in dxy:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                arr[ni][nj] = 2
                day = visited[ni][nj] - 1
    for k in range(N):
        for m in range(N):
            if arr[k][m] == 0 or (arr[k][m] == 2 and visited[k][m] == 0):
                is_spread = False
                break
        if not is_spread:
            break

    return day, is_spread


def zohap(i, n, K):
    try:
        global min_day
        if i > n:
            return
        if K == 0:
            start_list = deque()
            for j in range(n):
                if bit[j] == 1:
                    start_list.append(start[j])

            day, is_spread = bfs(arr, start_list)
            if is_spread:
                min_day = min(min_day, day)
        else:
            bit[i] = 1
            zohap(i + 1, n, K - 1)
            bit[i] = 0
            zohap(i + 1, n, K)
    except:
        pass


dxy = [[0, -1], [1, 0], [-1, 0], [0, 1]]
N, M = map(int, sys.stdin.readline().split())
arr = []

start = deque()
for i in range(N):
    ad = list(map(int, sys.stdin.readline().split()))
    arr.append(ad)
    for j in range(N):
        if ad[j] == 2:
            # 바이러스를 놓을 수 있는 지점
            start.append((i, j))

bit = [0] * len(start)
min_day = 10000000000000
zohap(0, len(start), M)
if min_day == 10000000000000:
    print(-1)
else:
    print(min_day)
