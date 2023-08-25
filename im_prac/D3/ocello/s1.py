import sys
sys.stdin = open("input.txt")

dxy = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]


def play(i,j,color):
    board[i][j] = color
    stack = []
    # 현재 위치 i,j 색깔
    dir = []
    for di, dj in dxy:
        distance = 0
        while 1:
            distance += 1
          # 8방향을 순회하며

            ni = i + di * distance
            nj = j + dj * distance
            # 새로운 인덱스가 범위 안에 있고 다음 인덱스가 0이 아니면
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] != 0:
                # 근데 색깔이 다르면
                if color != board[ni][nj]:
                    stack.append([ni,nj,di,dj,board[ni][nj]])     # 현재위치, 방향, 스택에 쌓아줍니다..

                # 만약 같은색의 돌을 만나면 탈출
                else:

                    stack.append([ni,nj,di,dj,color])
                    break
            else:   # 범위안에 없거나 다음인덱스가 0이면
                # 다음 수행...
                break
    # 스택안에 있는 돌들을 다 꺼내면서 그 색의 돌로 바꿔준다
    # 스택 안을 돌면서 color가 현재꺼랑 같은 di ,dj를 찾아서 방향 리스트에 넣어준다
    for s in stack:
        if s[-1] == color:
            dir.append([s[2],s[3]])
    if dir:
        # 스택을 돌면서
        for s in stack:
            # 같은 방향에 쌓인 돌들을
            if [s[2],s[3]] in dir:
                # 바꿔줍니다
                board[s[0]][s[1]] = color



B = 1
W = 2


T = int(input())

for tc in range(1, T+1):
    # 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
    # 각 테스트 케이스의 첫 번째 줄에는 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M
    N,M= map(int,input().split())
    arr = [list(map(int, input().split())) for i in range(M)]
    board = [[0]*N for i in range(N)]
    # 가운데 초기 상태
    board[N//2][N//2] = W
    board[N//2-1][N//2-1] = W
    board[N//2][N//2-1] = B
    board[N//2-1][N//2] = B


    # 주어진 돌을 놓는다
    for i in range(M):
        play(arr[i][0]-1,arr[i][1]-1,arr[i][2])

    cntb = 0
    cntw = 0
    # 보드판을 순회하면서 돌을 세준다
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                cntb += 1
            elif board[i][j] == W :
                cntw += 1


    print(f'#{tc} {cntb} {cntw}')