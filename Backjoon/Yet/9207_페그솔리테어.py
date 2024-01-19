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

    new_pins = []
    # 새로운 핀 위치
    for r in range(len(board)):
        for c in range(len(board[0])):
            if arr_copy[r][c] =='o':
                new_pins.append((r,c))

    return arr_copy,new_pins


def bfs(hole,arr):
    """
    각 핀이 있는 칸들을 돌아가면서 수직수평으로
    이동할 수 있는 경우들을  큐에 담아 bfs로 확인하며
    dp[핀의 개수]를 최소 이동횟수로 갱신한다
    """
    q = deque([[arr, hole, 0]])
    while q:
        board, pins, cnt = q.popleft()
        for pin in pins:
            i,j = pin
            for di,dj in dir:
                ni = i + di
                nj = j + dj
                nni = i + di*2
                nnj = j + dj*2
                if can_switch(board,[i,j],[ni,nj],[nni,nnj]):
                    new_arr,new_pins = rotate(board,[i,j],[ni,nj],[nni,nnj])
                    q.append([new_arr,new_pins,cnt+1])
                    dp[len(new_pins)] = min(dp[len(new_pins)],cnt+1)







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
    bfs(hole,arr)
    for i in range(1,len(hole)+1):
        if dp[i] != 100000000000:
            print(i, dp[i])
            break

