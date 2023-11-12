from collections import deque
import copy


def toggle_color(fin_board,i, j):
    board = copy.deepcopy(fin_board)
    for di, dj in [[0, 1], [-1, 0], [1, 0], [0, -1],[0,0]]:
        ni = di + i
        nj = dj + j
        if 0 <= ni < 3 and 0 <= nj < 3:
            if board[ni][nj] == '*':
                board[ni][nj] = '.'
            else:
                board[ni][nj] = '*'
    return board

def turn_to_binary(board):
    board_binary = ''
    for i in range(3):
        for j in range(3):
            if board[i][j] == ".":
                board_binary += '0'
            else:
                board_binary += '1'
    return int(board_binary,2)

def bfs(board):
    cnt = 0
    start_board = [['.']*3 for _ in range(3)]
    visited = [0]*1000

    q = deque()
    q.append(start_board)
    visited[turn_to_binary(start_board)] = 1

    while q:
        q_length = len(q)
        for _ in range(q_length):
            now_board = q.popleft()

            if now_board == board:
                return cnt

            for i in range(3):
                for j in range(3):
                    next_board = toggle_color(now_board,i,j)
                    binary_next_board = turn_to_binary(next_board)

                    if not visited[binary_next_board]:
                        q.append(next_board)
                        visited[binary_next_board] = 1
        cnt += 1

def solution(t):
    time = bfs(t)
    return time


T = int(input())
for _ in range(T):

    end_board = [list(input()) for _ in range(3)]
    toggle_cnt = solution(end_board)
    print(toggle_cnt)
