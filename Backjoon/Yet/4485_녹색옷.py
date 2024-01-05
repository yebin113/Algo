from collections import deque
import sys
input = sys.stdin.readline


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


dir = [[0,1],[1,0],[-1,0],[0,-1]]
t = 0
while 1:
    t += 1
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int,input().split())) for _ in range(n)]
    dp = [[125*n*n]*n for _ in range(n)]
    dp[0][0] = cave[0][0]
    for i in range(1,n):
        dp[0][i] = dp[0][i-1] + cave[0][i]
        dp[i][0] = dp[i-1][0] + cave[i][0]
    dp[1][1] = dp[0][0] + min(dp[1][0],dp[0][1]) + cave[1][1]
    for k in range(n):
        print(cave[k],'         ',dp[k])
    print()
    for i in range(1,n):
        for j in range(1,n):
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + cave[i][j]
            for k in range(n):
                print(cave[k],'         ',dp[k])
            print()
    ans = dp[-1][-1]




    print(f'Problem {t}: {ans}')

#
# def dfs(i,j,rupee,path):
#     print(i,j)
#     global ans
#     if i == n-1 and j == n-1:
#         ans = min(ans, rupee)
#     for direction in dir:
#         di,dj = direction
#         ni = i + di
#         nj = j + dj
#         # 범위 밖 제외
#         if ni < 0 or ni >= n or nj < 0 or nj >= n or (ni,nj) in path:
#             continue
#
#         dfs(ni,nj,rupee+cave[ni][nj],path+[(ni,nj)])
#
#
# dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
# t = 0
# while 1:
#     t += 1
#     n = int(input())
#     if n == 0:
#         break
#     cave = [list(map(int, input().split())) for _ in range(n)]
#     ans = 10000000000000000000000000000000000000000
#     dfs(0,0,cave[0][0],[(0,0)])
#     print(f'Problem {t}: {ans}')