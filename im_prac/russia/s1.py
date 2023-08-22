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
    print(f'윗줄 아랫줄 칠함 {paint_sum}')
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
        print(total_white)
        print(total_blue)
        print(total_red)
        # 각 리스트를 훑어봄
        i = 0
        while visited[i] == 0 and total_white[i] > total_blue[i] or (i+1 < mid_len and total_white[i] == total_blue[i] and total_white[i+1] > total_blue[i+1]):
            # 칠하고
            paint_sum += M - total_white[i]
            # 방문표시
            visited[i] = 'W'
            print(f'{i}번째 흰줄 칠함 {paint_sum}')
            i += 1
            if i == mid_len:
                break

        last_white = i
        print(f'마지막 흰줄 {last_white}')
        i = 0
        # 밑에서부터 빨간색이 많으면 칠하기
        while visited[i] == 0 and total_red[mid_len - 1 - i] > total_blue[mid_len - 1 - i] or (i+1 < mid_len and total_red[i] == total_blue[i] and total_red[i+1] > total_blue[i+1]) :
            # 칠하고
            paint_sum += M - total_red[mid_len - 1 - i]
            # 방문표시
            visited[i] = 'R'
            print(f'{mid_len - 1 - i}번째 빨간줄 칠함 {paint_sum}')
            if i == mid_len:
                break

        last_red = mid_len - i
        print(f'마지막 빨간줄 {last_red}')


        if last_white == last_red:      # 만약 파랑이가 칠해질 곳이 없다면
            print('파랑이 없어요')
            if total_blue[last_white] > total_blue[last_white+1]:
                paint_sum = paint_sum + total_white[last_white] - total_blue[last_white]
            else:
                paint_sum = paint_sum + total_white[last_white+1] - total_blue[last_white+1]
        else:

            for i in range(last_white,last_red):
                paint_sum += M - total_blue[i]  # 아니면 파랭이 칠해주기
                print(f'{i}번째 파란줄 칠함 {paint_sum}')

    print(f'#{tc} {paint_sum}')
