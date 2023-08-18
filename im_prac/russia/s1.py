"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQl9TIK8qoDFAXj
"""

import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for i in range(N)]
    visited = [0] * N
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
        total_white = []
        total_blue = []
        total_red = []
        for i in range(1, N - 1):
            count_W = 0
            count_B = 0
            count_R = 0
            # 그 줄의 색 몇개인지 세기
            for j in range(M):
                if arr[i][j] == "W":
                    count_W += 1
                elif arr[i][j] == "R":
                    count_R += 1
                else:
                    count_B += 1
            total_white.append(count_W)
            total_blue.append(count_B)
            total_red.append(count_R)
        mid_len = len(total_white)
        # 각 리스트를 훑어봄
        for i in range(mid_len):
            # 위에서부터 흰색이 많으면 흰색 칠하기
            if total_white[i] > total_blue[i] and visited[i] == 0:
                # 칠하고
                paint_sum += M - total_white[i]
                # 방문표시
                visited[i] = 'W'
            else:
                last_white = i
                break
        for i in range(mid_len):
            # 밑에서부터 빨간색이 많으면 칠하기
            if total_red[mid_len - 1 - i] > total_blue[mid_len - 1 - i] and visited[i] == 0:
                # 칠하고
                paint_sum += M - total_red[i]
                # 방문표시
                visited[i] = 'R'
            else:
                last_red = i
                break
        if last_white == last_red:      # 만약 파랑이가 칠해질 곳이 없다면
            if total_blue[last_white] > total_blue[last_white+1]:
                paint_sum = paint_sum + total_white[last_white] - total_blue[last_white]
            else:
                paint_sum = paint_sum + total_white[last_white+1] - total_blue[last_white+1]
        else:
            for i in range(last_white,last_red):
                paint_sum += M - total_blue[i]  # 아니면 파랭이 칠해주기

    print(f'#{tc} {paint_sum}')
