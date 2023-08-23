"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18LoAqItcCFAZN
"""

import sys

sys.stdin = open("input.txt")

# 1. 새로운 시작점을 찾는 함수
def start(arr,visited):
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and visited[i][j] == 0:
                return i,j
    # 이제 조사할 곳이 없으면 -1을 리턴합니다
    return -1,-1

T = int(input())

for tc in range(1, T + 1):
    # 저장된 창고 크기
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    visited = [[0]*N for i in range(N)]
    dim_list = []


    while 1:
        # 시작점을 찾는다
        i,j = start(arr,visited)
        # 종료조건
        if i== -1:
            break
        # 시작 위치 체크
        sti = i
        stj = j
        # 2. 다음 칸이 범위 안에 있고, 0이 아니며, 방문하지 않은 곳이라면,
        while j + 1 < N and arr[i][j+1] != 0 and visited[i][j+1] == 0:

            visited[i][j+1] = 1     # 방문표시
            j += 1                  # 현재 위치 옮기기

        # 3. 다음 줄이 범위 안에 있고, 0이 아니며, 방문하지 않은 곳이라면,
        while i + 1 < N and arr[i+1][j] != 0 and visited[i+1][j] == 0:

            visited[i+1][j] = 1  # 방문표시
            i += 1  # 현재 위치 옮기기

        # 끝난 위치 체크
        fin_i = i
        fin_j = j

        # 4. ㄱ자로 내려왔으니 그 범위를 다 방문표시 해주기
        for i in range(sti,fin_i+1):
            for j in range(stj,fin_j+1):
                visited[i][j] = 1
        # 5. 행렬 정보 저장 -> 정렬을 위해 첫번째는 행렬 크기, 두번째는 행 수, 세번째는 열 수
        ## 크기가 같을 경우 행이 작은 순으로 출력한다. <- 놓쳤던 조건
        dim_list.append([(fin_j-stj+1)*(fin_i-sti+1),fin_i-sti+1,fin_j-stj+1])

        if i == N-1 and j == N-1:
            break
    # 정렬
    dim_list.sort()
    # 정렬 후 행과 열만 뽑을것
    new_list = []
    for dim in dim_list:
        new_list.append(dim[1])
        new_list.append(dim[2])
    # 맨 앞에 총 나온 행렬 갯수도 넣어야 함 <- 놓친 문제 조건 2
    new_list.insert(0,len(dim_list))
    print(f'#{tc}',*new_list)




