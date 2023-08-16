"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQl9TIK8qoDFAXj
"""

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(input()) for i in range(N)]
    paint_sum = 0
    for j in range(M):
        # 시작줄이 흰색이 아니면 칠함
        if arr[0][j] != 'W':
            paint_sum += 1
        # 마지막줄이 빨간색이 아니면 칠함
        if arr[-1][j] != 'R':
            paint_sum += 1
    # 3줄이면 무조건 흰 파 빨
    if N == 3:
        for j in range(M):
            # 시작줄이 파란색이 아니면 칠함
            if arr[1][j] != 'B':
                paint_sum += 1
    # 3줄이 아니면
    else:
        # 가운뎃 줄
        for i in range(1,N-1):
            count_W = 0
            count_B = 0
            count_R = 0
            for j in range(M):
                if arr[i][j] == "W":
                    count_W += 1
                elif arr[i][j] == "R":
                    count_R += 1
                else:
                    count_B +=1



    print(f'#{tc}')