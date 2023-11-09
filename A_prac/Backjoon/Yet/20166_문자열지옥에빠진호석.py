def dfs(x,y):
    visited = [(x,y)]
    for k in range(8):
        ni = x + dxy[k][0]
        nj = y + dxy[k][1]
        # 환형
        if ni >= N:
            ni -= N
        if nj >= M:
            nj -= M
        if ni < 0:
            ni += N
        if nj < 0:
            nj += M







dxy = [[0,1],[-1,0],[1,0],[0,-1],[-1,1],[-1,-1],[1,-1],[1,1]]
N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
god_like = [input() for _ in range(M)]

