import sys

sys.stdin = open("input.txt")

T = int(input())
# 좌하 , 우하
dir = [[1, -1], [1, 1]]
for tc in range(1, T + 1):
    # 한변의 길이
    N = int(input())
    # 디저트 카페
    arr = [list(map(int, input().split())) for i in range(N)]
    # 각 루트들을 저장
    total_route = []
    # 중간 index들만 가능
    for i in range(N - 1):
        for j in range(1, N - 1):
            flag = True
            # 루트를 리스트화 시킬것..
            route = [arr[i][j]]
            # 왼쪽으로 갈 수 있는 횟수
            for k in range(j):
                # 좌 하 인덱스
                left_ni = i + 1
                left_nj = j - 1
                # 우 하 인덱스
                right_ni = i
                right_nj = j
                if arr[left_ni][left_nj] in route:
                    flag = False
                    break
                route.append(arr[left_ni][left_nj])
                print('시작 왼쪽 대각선 ',i,j,left_ni,left_nj,route)
                route_new = route[:]
                # 범위 벽세우기
                while right_nj < N-1 and left_ni < N-1:
                    # 우 하로 향하는..
                    left_ni = left_ni + 1
                    left_nj = left_nj + 1
                    right_ni = right_ni + 1
                    right_nj = right_nj + 1
                    if arr[left_ni][left_nj] in route_new or arr[right_ni][right_nj] in route_new:
                        flag = False
                        break
                    route_new.append(arr[left_ni][left_nj])
                    route_new.append(arr[right_ni][right_nj])
                    if flag == True:
                        total_route.append(route_new)

                if flag == True:
                    total_route.append(route_new)
    print('최종 루트',total_route)
    ans = 0
    if len(total_route) == 0:
        ans = -1
    else:
        for i in range(len(total_route)):
            ans = max(ans,sum(total_route[i]))

    print(f'#{tc} {ans}')
