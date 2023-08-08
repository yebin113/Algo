"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18LoAqItcCFAZN
"""

import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # 저장된 창고 크기
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    # 차원 행렬 저장
    dim_list = []

    little_arr = []
    i = 0
    j = 0

    while i < N and j < N:

        little_row = []

        while arr[i][j] != 0:
            # 다음칸이 0이 아니면
            if arr[i][j + 1] >= 1:
                # 행 요소에 추가
                little_row.append(arr[i][j])
                # 열 인덱스를 하나 늘려줌
                j += 1
            # 다음칸이 0이 아니고 다음 줄이 존재한다면
            elif arr[i + 1][j] >= 1:
                # 요소를 늘려줌
                little_arr.append(little_row)
                # 다음줄로 넘어감
                i += 1

        dim_list.append(len(little_arr[0]))
        dim_list.append(len(little_arr)-1)
        print(dim_list)
        i += 1
        j += 1


