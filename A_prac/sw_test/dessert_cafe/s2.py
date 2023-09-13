import sys

sys.stdin = open("input.txt")

import sys

sys.stdin = open("input.txt")



T = int(input())
# 좌하 -> 우하 -> 우상 -> 좌상
dir = [[1, -1],[1, 1] , [-1, 1],[-1, -1]]
for tc in range(1, T + 1):
    # 한변의 길이
    N = int(input())
    # 디저트 카페
    arr = [list(map(int, input().split())) for i in range(N)]
    total_route = []
    max_dessert = -1
    # 열 2칸 전까지 가능함
    for i in range(N - 3):
        # 행 맨앞 맨뒤 안됨..
        for j in range(1, N - 1):
            # 루트 작성
            route = [arr[i][j]]

            for k in range(1,min(j+1,N-i)):
                # 왼쪽으로 오는길
                left_ni = i + k
                left_nj = j - k
                right_ni = i
                right_nj = j
                route.append(arr[left_ni][left_nj])
                # 오른쪽길

                for m in range(1,min(N-i,N-j)-i):
                    right_ni = right_ni + 1
                    right_nj = right_nj + 1
                    left_ni = left_ni + 1
                    left_nj = left_nj + 1
                    route.extend([arr[right_ni][right_nj],arr[left_ni][left_nj]] )
                    for l in range(1, k):
                        # 왼쪽으로 오는길
                        last_right_ni = right_ni + l
                        last_right_nj = right_nj - l
                        route.append(arr[last_right_ni][last_right_nj])
                    total_route.append(route)
                    for l in range(1,k):
                        # 왼쪽으로 오는길
                        last_right_ni = right_ni + l
                        last_right_nj = right_nj - l
                        route.remove(arr[last_right_ni][last_right_nj])

                route = route[:1+k]
    if len(total_route) == 0:
        print(f'#{tc} {max_dessert}')
    else:
        for rout in total_route:
            flag = True
            for i in range(len(rout)):
                if rout.count(rout[i]) > 1:
                    flag = False
            if flag == True:
                if max_dessert < len(rout):
                    max_dessert = len(rout)

        print(f'#{tc} {max_dessert}')

#
# T = int(input())
# # 좌하 -> 우하 -> 우상 -> 좌상
# dir = [[1, -1],[1, 1] , [-1, 1],[-1, -1]]
# for tc in range(1, T + 1):
#     # 한변의 길이
#     N = int(input())
#     # 디저트 카페
#     arr = [list(map(int, input().split())) for i in range(N)]
#     total_route = []
#     max_dessert = -1
#     # 열 2칸 전까지 가능함
#     for i in range(N - 2):
#         # 행 맨앞 맨뒤 안됨..
#         for j in range(1, N - 1):
#             # 루트 작성
#             route = [arr[i][j]]
#             # print('시작점',i,j)
#             for k in range(1,j+1):
#                 # 왼쪽으로 오는길
#                 left_ni = i + k
#                 left_nj = j - k
#                 right_ni = i
#                 right_nj = j
#                 route.append(arr[left_ni][left_nj])
#                 for m in range(1,N-j-i):
#                     right_ni = right_ni +1
#                     right_nj = right_nj +1
#                     left_ni = left_ni + 1
#                     left_nj = left_nj + 1
#                     route.extend([arr[right_ni][right_nj],arr[left_ni][left_nj]] )
#                     for l in range(1, k):
#                         # 왼쪽으로 오는길
#                         last_right_ni = right_ni + l
#                         last_right_nj = right_nj - l
#                         route.append(arr[last_right_ni][last_right_nj])
#                     print(route)
#                     total_route.append(route)
#                     for l in range(1, k):
#                         # 왼쪽으로 오는길
#                         last_right_ni = right_ni + l
#                         last_right_nj = right_nj - l
#                         route.remove(arr[last_right_ni][last_right_nj])
#                     # print(route)
#
#                 route = route[:1+k]
#     max_route = -1
#
#     if len(total_route) == 0:
#         print(f'#{tc} {max_route}')
#     else:
#         for i in range(len(total_route)):
#             if len(total_route[i]) == len(list(set(total_route[i]))):
#                 length = len(total_route[i])
#                 if max_route < length:
#                     max_route = length
#         print(f'#{tc} {max_route}')
