from collections import deque


def bfs():

    dp = [0]*(N*N)
    dp[0] = 1
    q = deque()
    q.append((0, 0))

    while q:
        fi, fj = q.popleft()
        if fi == N-1 and fj == N-1:
            continue
        for di, dj in [[0, 1], [1, 0]]:
            ni = fi + di * arr[fi][fj]
            nj = fj + dj * arr[fi][fj]
            # print(ni,nj)
            if 0 <= ni < N and 0 <= nj < N:
                dp[ni*N+nj] = dp[ni*N+nj] + 1
                q.append((ni,nj))
                # print(q)
    return dp[-1]


import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(bfs())
# 우 하 로 이동하면서 현재로 올수 있는 가짓수를 구함...
