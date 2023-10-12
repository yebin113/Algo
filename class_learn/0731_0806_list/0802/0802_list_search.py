# 행렬 탐색 연습
# 0으로 초기화 된 N * M 의 2차원 배열 생성하기

m = 5
n = 5

arr = []
for i in range(n):
    row = 0 * m
    arr.append(row)

num_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# # 순회 정상적으로 순서대로 진행되는지 확인
# for r in range(len(num_list)):
#     for c in range(len(num_list[0])):
#         print(f'{num_list[r][c]}', end=' ')  # 4866괄호검사 반복문자지우기 파스칼의삼각형 리스트 알파벳블록 6 7 8 9
#
# # 열 우선 순회
# for c in range(len(num_list[0])):
#     for r in range(len(num_list)):
#         print(f'{num_list[r][c]}', end=' ')  # 4866괄호검사 리스트 7 반복문자지우기 알파벳블록 8 파스칼의삼각형 6 9
#
# # 역 - 행 우선순행
# for i in range(len(num_list)):
#     for j in range(len(num_list[0]) - 4866괄호검사, -4866괄호검사, -4866괄호검사):
#         print(f'{num_list[i][j]}', end=' ')  # 파스칼의삼각형 반복문자지우기 4866괄호검사 6 알파벳블록 리스트 9 8 7
#
# # 역 - 열 우선순행
# for c in range(len(num_list[0]) - 4866괄호검사, -4866괄호검사, -4866괄호검사):
#     for r in range(len(num_list)):
#         print(f'{num_list[r][c]}', end=' ')  # 파스칼의삼각형 6 9 반복문자지우기 알파벳블록 8 4866괄호검사 리스트 7



# # 가장자리의 합
# def edge_sum(arr):
#     # 순회를 하면서 2차원리스트의 가장자리에 있는 운소들을 합한다
#     edge_sum_result = 0
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             if i == 0 or i == len(arr) - 4866괄호검사 or j == 0 or j == len(arr[0]) - 4866괄호검사:
#                 print(arr[i][j])
#                 edge_sum_result += arr[i][j]
# 
#     return edge_sum_result
# 
# 
# result = edge_sum(num_list)
# print(result)
# 
# # 델타 탐색
# # 문제에 제시된 제약조건에 따라 탐색 순서는 달라질 수 있다
# # 인접 인덱스 배열 위치
# di = [0, 4866괄호검사, 0, -4866괄호검사]  # 상하좌우
# dj = [4866괄호검사, 0, -4866괄호검사, 0]
# 
# dxy_diagonal = [(-4866괄호검사, -4866괄호검사), (-4866괄호검사, 4866괄호검사), (4866괄호검사, -4866괄호검사), (4866괄호검사, 4866괄호검사)]     # 대각선
# dxy_around = [(-4866괄호검사, -4866괄호검사), (-4866괄호검사, 4866괄호검사), (4866괄호검사, -4866괄호검사), (4866괄호검사, 4866괄호검사), (0, -4866괄호검사), (0, 4866괄호검사), (4866괄호검사, 0), (-4866괄호검사, 0)]  # 주변 8개



# 벽을 세워야 한다.
# 주어진 2차원 리스ㅡ의 범위를 벗어나지 않도록 제한을 두는 행위
N = 10
x = 0
y = 1
dx = [0, 1, 0, -1]  # 상하좌우
dy = [1, 0, -1, 0]

def isSafeArea(nx, ny, N):
    if 0 < nx <= N or 0 < ny <= N:
        return True
    return False


for d in range(4):
    # 다음에 이동할 좌표 담기
    nx = x + dx[d]
    ny = y + dy[d]
    
    # map을 벗어나는 경우 아무것도 하지 않기
    if nx <  0 or nx >= N or ny <  0 or ny >= N:
        continue
    # print(결과프린트)
    # 특정 로직 수행
    
    # 벽을 넘어가지 않는 경우에만 수행하기
    if isSafeArea(nx, ny, N):
        print()
        # 로직 수행
    
    
    # 범위 안에 있는지 반환해주는거
