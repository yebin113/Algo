import sys
import copy
from collections import deque

input = sys.stdin.readline
"""
 '.'는 빈 칸, 'o'는 핀이 꽂혀있는 칸, 
 '#'는 구멍이 없는 칸
"""


def can_switch(board, spot, nspot, nnspot):
    i, j = spot
    len_n, len_m = len(board), len(board[0])
    ni, nj = nspot
    nni, nnj = nnspot
    # print(f'len_n {len_n}, len_m {len_m}, ni {ni}, nni {nni}, nj {nj}, nnj {nnj}')
    # 범위 내에 있고 인접칸에 핀이 있고 그 다음이 빈칸이라면
    if 0 <= ni < len_n and 0 <= nj < len_m and 0 <= nni < len_n and 0 <= nnj < len_m and board[ni][nj] == 'o' and board[nni][nnj] == '.':
        return True
    else:
        return False


def rotate(board, spot, nspot, nnspot):
    i, j = spot
    arr_copy = copy.deepcopy(board)
    ni, nj = nspot
    nni, nnj = nnspot
    arr_copy[i][j] = '.'
    arr_copy[ni][nj] = '.'
    arr_copy[nni][nnj] = 'o'
    return arr_copy


def bfs(hole):
    """
    각 핀이 있는 칸들을 돌아가면서 수직수평으로
    이동할 수 있는 경우들을  큐에 담아 bfs로 확인하며
    dp[핀의 개수]를 최소 이동횟수로 갱신한다
    """
    q = deque()
    for h in hole:
        q.append((arr,h[0],h[1],len(hole),0))

    while q:
        board, i, j, cnt, switch = q.popleft()
        for d in dir:
            di, dj = d
            ni, nj = i + di, j + dj
            nni, nnj = i + di * 2, j + dj * 2
            if can_switch(board, [i, j], [ni, nj], [nni, nnj]):
                n_board = rotate(board, [i, j], [ni, nj], [nni, nnj])
                q.append([n_board, nni, nnj, cnt -1, switch + 1])
                dp[cnt-1] = min(switch +1,dp[cnt-1])


N = int(input())
dir = [[0, 1], [-1, 0], [1, 0], [0, -1]]
for _ in range(N):
    arr = []
    hole = []
    while 1:
        n = list(input().rstrip())
        if len(n) == 0:
            break
        arr.append(n)

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'o':
                hole.append((i,j))

    dp = [100000000000]*(len(hole)+1)
    dp[-1] = 0
    bfs(hole)
    for i in range(1,len(hole)+1):
        if dp[i] != 100000000000:
            print(i, dp[i])
            break