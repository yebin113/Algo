import sys
input = sys.stdin.readline
from collections import deque


def bfs():
    q = deque()
    q.append([hi-1,hj-1,0,1])
    visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]
    visited[1][hi-1][hj-1] = True
    while q:
        i,j,time,key = q.popleft()
        if i==ei-1 and j==ej-1:
            return time
        for i in range(4):
            ni = i+di[i]
            nj = j+dj[i]
            if 0<=ni<N and 0<=nj<M:
                if key:
                    if maze[ni][nj] == 0:
                        if not visited[1][ni][nj]:
                            visited[1][ni][nj] = True
                            q.append([ni,nj,time+1,key])
                    elif maze[ni][nj] == 1:
                        if not visited[0][ni][nj]:
                            visited[0][ni][nj] = True
                            key = 0
                            q.append([ni,nj,time+1,key])
                            key = 1
                elif not key:
                    if not visited[0][ni][nj]:
                        if not maze[ni][nj]:
                            visited[0][ni][nj] = True
                            q.append([ni,nj,time+1,key])
    return -1

N, M = map(int, input().split())
hi,hj = map(int, input().split())
ei,ej = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

di = [0,0,1,-1]
dj = [1,-1,0,0]
print(bfs())


# from collections import deque
# import copy
# def bfs():
#     global cnt,check
#     q = deque()
#     q.append([hi,hy,0,1])
#     visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]
#     visited[1][hi - 1][hy - 1] = True
#     while q:
#         i,j,time,key = q.popleft()
#         if i == ei and j == ey:
#             cnt = min(cnt,time)
#             check = True
#             return
#         for di,dj in dir:
#             ni = i + di
#             nj = j + dj
#
#             if not(0<=ni<N and 0<=nj<M):
#                 continue
#             if key:
#
#                 if maze[ni][nj] == 0:
#                     if visited[1][ni][nj]:
#                         visited[1][ni][nj] = True
#                         q.append([ni, nj, time + 1, key])
#                 elif maze[ni][nj]:
#                     if not visited[0][ni][nj]:
#                         visited[0][ni][nj] = True
#                         key = 0
#                         q.append([ni, nj, time + 1, key])
#                         key = 1
#             elif not key:
#                 if not visited[0][ni][nj]:
#                     if not maze[ni][nj]:
#                         visited[0][ni][nj] = True
#                         q.append([ni, nj, time + 1, key])
#
#
# dir = [[0, 1], [-1, 0], [1, 0], [0, -1]]
# N,M = map(int,input().split())
# hi,hy = map(int,input().split())
# hi -= 1
# hy -= 1
# ei,ey = map(int,input().split())
# ei -= 1
# ey -= 1
# cnt = N*M
# check = False
# maze = []
# for _ in range(N):
#     maze.append(list(map(int,input().split())))
# bfs()
#
# if check:
#     print(cnt)
# else:
#     print(-1)