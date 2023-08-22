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
    visited = [[0]*N for i in range(N)]
    dim_list = []
    i = 0
    j = 0
    dim_x = 1
    dim_j = 0
    while i < N and j < N:
        # 만약 빈용기가 아니고 방문한 곳이 아닐때
        while 0<=j<N and arr[i][j]!= 0 and visited[i][j] == 0:
            print(f'여기는 {i}번째{j}칸 빈용기가 아님')
            # 방문표시
            visited[i][j] = 1
            # 가로행렬 표시
            dim_j += 1
            # 다음이 빈용기가 아닐때까지 다음으로 이동
            j += 1
            # 다음이 아니면 i줄 저장해둠
            if j+1 >= N or arr[i][j+1]== 0 or visited[i][j+1] != 0:
                j -= 1
                kumsa_i = i

        # 밑에줄이 범위 밖이거나 빈용기가 아닐때까지
        while 0 <= i+1 < N and arr[i+1][j] != 0 and visited[i+1][j] == 0:
            # 행렬 정보
            dim_x +=1
            i += 1
            # 방문표시
            visited[i][j] = 1
            # 다음줄이 비었을때
            if i+1 >= N or arr[i+1][j]== 0 or visited[+1][j] != 0:
                j += 1
                i = kumsa_i
                # 행렬 정보 넣기
                dim_list.append(dim_x * dim_j)

                # 초기화
                dim_j = 0
                dim_x = 1

        print(visited)

        j += 1
        if j == N:
            i += 1
            j = 0

    print(dim_list)


