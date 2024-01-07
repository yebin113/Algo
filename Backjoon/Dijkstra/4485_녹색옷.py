from collections import deque
import heapq
import sys
input = sys.stdin.readline


def dijkstra(N,arr):
    q = []
    visited = [[int(1e9)] * n for _ in range(n)]

    heapq.heappush(q, (arr[0][0], 0, 0))
    while q:
        rupee, i, j = heapq.heappop(q)
        # 끝에 도착했을때 return
        if i == n - 1 and j == n - 1:
            return visited[-1][-1]

        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            n_rupee = rupee + arr[ni][nj]
            if n_rupee < visited[ni][nj]:
                visited[ni][nj] = n_rupee
                heapq.heappush(q,(n_rupee,ni,nj))


dir = [[0,1],[1,0],[-1,0],[0,-1]]
t = 0
while 1:
    t += 1
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int,input().split())) for _ in range(n)]
    ans = dijkstra(n,cave)

    print(f'Problem {t}: {ans}')


def bfs(N,arr):
    q = deque([(0,0,0,-1)])
    visited = [[0]*N for _ in range(N)]
    visited[0][0] = arr[0][0]
    while q:
        i,j,li,lj = q.popleft()
        for di,dj in dir:
            ni = i + di
            nj = j + dj
            # 범위 밖 제외 또는 방금 지나온 길은 제외
            if ni < 0 or ni >= N or nj < 0 or nj >= N or (li==ni and lj == nj):
                continue
            # 아직 방문하지 않았거나, 지금 온 경로보다 더 빼앗긴 루피가 크다면 갱신
            if visited[ni][nj] == 0 or visited[ni][nj] > visited[i][j] + arr[ni][nj]:
                q.append((ni,nj,i,j))
                visited[ni][nj] = visited[i][j] + arr[ni][nj]
        for k in range(N):
            print(visited[k])
        print()
    return visited[-1][-1]

