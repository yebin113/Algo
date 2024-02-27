import sys
input = sys.stdin.readline
# 1,2,3 각 숫자로 끝나는 경우
dp = [[0 for _ in range(3)] for _ in range(100001)]
# 1로 끝나는 [1]
dp[1] = [1, 0, 0]
# 2로 끝나는 [2]
dp[2] = [0, 1, 0]
# 1로 끝나는 [2,1] , 2로 끝나는 [1,2], 3으로 끝나는 [3]
dp[3] = [1, 1, 1]

# 미리 계산해두기
for i in range(4, 100001):
    # 1로 끝나는 경우는 지금 i 보다 1 작은 수가 2와 3으로 끝나는 경우를 합쳐준 것
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 1000000009
    # 2로 끝나는 경우는 지금 i 보다 2 작은 수가 1, 3으로 끝나는 경우를 합쳐준 것
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % 1000000009
    # 3으로 끝나는 경우는 지금 i 보다 3 작은 수가 1와 2으로 끝나는 경우를 합쳐준 것
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % 1000000009

T = int(input())
for i in range(T):
    n = int(input())
    # 사용
    print(sum(dp[n]) % 1000000009)



# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10000)
# """
# 정수 n이 주어졌을 때,
# n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
# dp로 도저히 모르겠어서 dfs로 깊이 탐색 시전..
# """
#
# def dfs(arr):
#     global cnt
#     array = list(map(int,arr))
#     if sum(array) > N:
#         return
#     elif sum(array) == N:
#         cnt += 1
#     else:
#         for i in range(1,4):
#             if i == int(arr[-1]):
#                 continue
#             dfs(arr+str(i))
#
#
#
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     cnt = 0
#     dfs("1")
#     dfs("2")
#     dfs("3")
#     print(cnt)
