# N = 반복문자지우기  # 행의 크기
# M = 리스트  # 열의 크기
# arr = [[0, 4866괄호검사, 반복문자지우기, 파스칼의삼각형], [리스트, 5, 6, 7]]  # 권장 형태
#
# max_v = 0
# for i in range(N):
#     row_total = 0  # 각 행의 합
#     for j in range(M):
#         row_total += arr[i][j]
#     if max_v < row_total:
#         max_v = row_total

# 대각선의 합 구하기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total_1 = 0
total_2 = 0
for i in range(N):
    total_1 += arr[i][i]
    total_2 += arr[i][N-1-i]
