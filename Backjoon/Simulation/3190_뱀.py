from collections import deque
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

N = int(input())
board = [[0] * N for _ in range(N)]
K = int(input())
# 사과저장
for _ in range(K):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 1

L = int(input())
move = []
for _ in range(L):
    x, c = map(str, input().split())
    move.append((int(x),c))

time = 0
d = 0
snake = [[0,0]]
move_time = 0
while 1:

    if move_time < len(move) and time == move[move_time][0]:
        # 방향 전환
        if move[move_time][1] == "L":
            d -= 1
            if d == -1:
                d = 3
        else:
            d += 1
            if d == 4:
                d = 0
        move_time += 1
    # 새로운 위치
    ni = snake[0][0] + dir[d][0]
    nj = snake[0][1] + dir[d][1]
    # 새로운 위치가 벽 밖이거나 자기자신의 몸이있는 곳이라면 끝
    if not (0<=ni<N and 0<= nj<N) or (ni,nj) in snake:

        break
    snake.insert(0,(ni,nj))
    # 사과를 안먹을 경우 마지막 꼬리 추가 x
    if board[ni][nj] != 1:
        snake.pop()
    else:
        board[ni][nj]= 0
    # 시간 추가
    time += 1


print(time+1)

