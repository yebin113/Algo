L,N,Q = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(L)]
knights = {}
for i in range(N):
    r,c,h,w,k = map(int,input().split())
    for i in range(r-1,r+h):
        for j in range(c-1,c+w):
            board[i][j] = f'k{i+1}'
    knights[f'k{i+1}'] = [r,c,h,w,k]
for i in range(L):
    print(board[i])

direct = {
    0:[-1,0],
    1:[0,1],
    2:[1,0],
    3:[0,-1]
}
for i in range(Q):
    num,dir = map(int,input().split())
