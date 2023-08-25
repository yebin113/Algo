def f(i,j,bw,N):    # 위치, 돌색, 보드판 크기
     # 돌을 놓기
    board[i][j] = bw
    for di, dj in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[0,-1],[-1,0],[-1,1]]:
        ni, nj = i +di, j +dj
        tmp = []
        while 0<=ni<N and 0<=nj<N and board[ni][nj] == op[bw]: # 보드 내부고 반대색이면 계속이동
            tmp.append((ni,nj))
            ni, nj = ni + di, nj+dj
        if 0<=ni<N and 0<=nj<N and board[ni][nj] == bw: # 보드 내부이고 같은색이면
            for p,q in tmp:
                board[p][q] = bw

"""
돌을 놓을 필요는 없음 입력으로 줌
"""
B = 1
W = 2
op = [0 , 2, 1]
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 보드 크기 N, 돌을 놓는 횟수 M
    N, M = map(int,input().split())
    # 짱구야 돌을 놓았어..
    arr = [list(map(int, input().split())) for i in range(M)]
    # 보드판
    board = [[0]*N for _ in range(N)]
    # 가운데 네자리 돌을 놓고 시작
    # 인덱스는 N//2 -1 ~ N//2
    board[N//2-1][N//2-1] = W
    board[N//2][N//2] = W
    board[N//2-1][N//2] = B
    board[N//2][N//2-1] = B
    # 입력이 col, row, color, row 는 인덱스 1 기준
    for col,row,bw in arr:
        f(row-1,col-1,bw,N)
    bcnt = wcnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                bcnt += 1
            elif board[i][j] == W:      # 빈칸도 있을수 있으니 elif 사용할 것
                wcnt += 1

    # 흑돌, 백돌 개수
    print(f'#{tc} {bcnt} {wcnt}')