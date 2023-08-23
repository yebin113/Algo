"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14BgD6AEECFAYh
"""

import sys
sys.stdin = open("input.txt")

T = 10

for _ in range(T):
    tc = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    arr_zero = [[0]*100 for i in range(100)]
    # 사다리타기를 할 수 있는 시작점
    start_point = []
    for j in range(100):
        if arr[0][j]:
            start_point.append(j)

    # 시작!
    for start in start_point:
        i = 0
        j = start
        distance = 0
        # 벽세우기
        while i < 100 and 0 <= j < 100:

            # 오른쪽이 1일때
            if arr[i][j+1] and 0 <= j+1 < 100 and arr_zero[i][j+1] == 0:
                print(f"현재위치 {i}번째줄 {j}칸 -> 오른쪽으로 이동, 거리 {distance}")
                j += 1
                distance += 1
                arr_zero[i][j] = 1
                while 0 <= j+1 < 100 and arr[i][j+1] and arr_zero[i][j+1] == 0:
                    print(f"현재위치 {i}번째줄 {j}칸 -> 오른쪽으로 이동, 거리 {distance}")
                    j += 1
                    distance += 1
                    arr_zero[i][j] = 1

            # 왼쪽이 1일때
            elif arr[i][j-1] and 0 <= j-1 < 100 and arr_zero[i][j-1] == 0:
                print(f"현재위치 {i}번째줄 {j}칸 -> 왼쪽으로 이동, 거리 {distance}")
                j -= 1
                distance += 1
                arr_zero[i][j] = 1
                while arr[i][j - 1] and 0 <= j-1 < 100:
                    print(f"현재위치 {i}번째줄 {j}칸 <- 왼쪽으로 이동, 거리 {distance}")
                    j -= 1
                    distance += 1
                    arr_zero[i][j] = 1

            else:
                i += 1
                distance += 1
                arr_zero[i][j] = 1
                print(f"현재위치 {i}번째줄 {j}칸 ^ 아래쪽으로 이동, 거리 {distance}")
                if i == 99:
                    break
        print(start, distance)





    # print(f'#{tc} {start_point}')