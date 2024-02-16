from collections import deque
def bfs():
    global ans
    q = deque()
    q.append(board)
    while 1:
        new_board = q.popleft()
        # 방향
        for di, dj in dir:
            # 1. 빈칸 옮기기
            starti = 0
            endi = N
            startj = 0
            endj = N
            stepi = 1
            stepj = 1
            if di == 1:
                starti = N-1
                endi = -1
                stepi = -1
            elif dj == 1:
                startj = N - 1
                endj = -1
                stepj = -1
            # 2. 합치기
            for i in range(starti,endi,stepi):
                for i in range(startj, endj, stepj):


dir = [[0,1],[1,0],[0,-1],[-1,0]]
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
ans = 0
print(ans)