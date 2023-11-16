from collections import deque


def bfs():

    dp = [[0]*N for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if i == N-1 and j == N-1:
                return dp[i][j]
            ni = i + arr[i][j]
            nj = j + arr[i][j]
            if ni < N:
                dp[ni][j] += dp[i][j]
            if nj < N:
                dp[i][nj] += dp[i][j]




import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(bfs())
# 우 하 로 이동하면서 현재로 올수 있는 가짓수를 구함...
