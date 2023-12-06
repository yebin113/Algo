import sys
sys.stdin = open("input.txt")
"""
DFS 활용
"""

import copy
def dfs(step, connected, board):
    # print(f'현재 {step}, 연결 셀 {connected} 시작전 보드')
    # for k in range(N):
    #     print(board[k])
    # print()

    global min_cnt,max_connected
    # 가지치기
    if len(locations) - step + connected < max_connected:
        return

    """
    :param step: 몇번째 셀을 하고 있나요?
    :param connected: 성공 셀 개수
    :param board: 현재 기판
    """
    if step == len(locations):
        # 만약 모든 셀을 다 연결햇다면 전선 개수 갱신
        cnt = 0
        for i in range(N):
            for j in range(N):
                if board[i][j] == 2:
                    cnt += 1
        if max_connected < connected:
            max_connected = connected
            min_cnt = cnt
        elif max_connected == connected:
            min_cnt = min(min_cnt,cnt)
        return
    else:
        for di, dj in dir:
            i = locations[step][0]
            j = locations[step][1]
            check = True
            # 가장자리까지 연결이 가능한지 확인
            while 0 <= i + di < N and 0 <= j + dj < N:
                i += di
                j += dj
                # 연결 불가능할때 break
                if board[i][j] != 0:
                    # print(f'현재 셀 {locations[step]} 현재 방향 {di,dj} 불가능')
                    check = False
                    break
            # 연결이 가능할때 재귀
            if check:
                dfs(step+1,connected+1,connect(di,dj,step,board))

        dfs(step+1,connected,board)



def connect(di,dj,step,array):
    arr1 = copy.deepcopy(array)
    i = locations[step][0]
    j = locations[step][1]
    # print(f'현재 셀 {i, j}, 현재 방향 {di, dj}')
    ni = i + di
    nj = j + dj

    while 0 <= ni < N and 0 <= nj < N:
        arr1[ni][nj] = 2
        ni += di
        nj += dj

    # for k in range(N):
    #     print(arr1[k])
    # print()
    return arr1




T = int(input())
dir = [[0, -1], [0, 1], [1, 0], [-1, 0]]

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_cnt = N * N
    max_connected = 0
    locations = []
    # 셀이 있는 장소 탐색
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if arr[i][j] == 1:
                locations.append([i, j])
    dfs(0,0,arr)
    print(f'#{tc} {min_cnt}')
