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

    min_distance = 10000
    min_start = 0
    distance_list = []
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
            while 0 <= j + 1 < 100 and arr[i][j + 1] and arr_zero[i][j + 1] == 0:
                # print(f"현재위치 {i}번째줄 {j}칸 -> 오른쪽으로 이동, 거리 {distance}")
                j += 1
                distance += 1
                arr_zero[i][j] = 1
            while arr[i][j - 1] and 0 <= j - 1 < 100 and arr_zero[i][j - 1] == 0:
                # print(f"현재위치 {i}번째줄 {j}칸 <- 왼쪽으로 이동, 거리 {distance}")
                j -= 1
                distance += 1
                arr_zero[i][j] = 1

            i += 1
            distance += 1
            arr_zero[i][j] = 1
            # print(f"현재위치 {i}번째줄 {j}칸 ^ 아래쪽으로 이동, 거리 {distance}")
            if i == 99:
                break
        distance_list.append([start, distance])
    for i in range(len(distance_list)):
        if min_distance > distance_list[i][1]:
            min_distance = distance_list[i][1]
            min_start = distance_list[i][0]
    print(tc, min_start)
