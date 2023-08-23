"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14BgD6AEECFAYh
틀린 부분:
방문 리스트를 시작점마다 초기화 시켜주지 않았다!
"""

import sys
sys.stdin = open("input.txt")

T = 10

for _ in range(T):
    tc = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]


    # 적게 가는 거리 갱신
    min_distance = 10000
    # 적게 가는 거리의 시작점 저장
    min_start = 0
    # 각 거리 리스트
    distance_list = []
    # 사다리타기를 할 수 있는 시작점
    start_point = []
    for j in range(100):
        if arr[0][j]:
            start_point.append(j)

    # 시작!
    for start in start_point:
        # 매 시작점마다 간 지점들 초기화 시켜줘야함
        arr_zero = [[0] * 100 for i in range(100)]
        # i는 0번째 줄에서 시작 j는 시작할 수 있는 지점에서 시작~
        i = 0
        j = start
        # 거리 0으로 초기화
        distance = 0
        # i가 99
        while i < 100:
            if 0 <= j + 1 < 100 and arr[i][j + 1] and arr_zero[i][j + 1] == 0:
                # 오른쪽으로 갈 수 있는 만큼 가기!
                while 0 <= j + 1 < 100 and arr[i][j + 1] and arr_zero[i][j + 1] == 0:
                    # print(f"현재위치 {i}번째줄 {j}칸 -> 오른쪽으로 이동, 거리 {distance}")
                    j += 1
                    distance += 1
                    arr_zero[i][j] = 1
            elif arr[i][j - 1] and 0 <= j - 1 < 100 and arr_zero[i][j - 1] == 0:
                # 왼쪽으로 갈 수 있을 만큼 가기
                while arr[i][j - 1] and 0 <= j - 1 < 100 and arr_zero[i][j - 1] == 0:
                    # print(f"현재위치 {i}번째줄 {j}칸 <- 왼쪽으로 이동, 거리 {distance}")
                    j -= 1
                    distance += 1
                    arr_zero[i][j] = 1
            else:
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
