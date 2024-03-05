# import sys
# sys.setrecursionlimit(100001)
from collections import deque

def bfs():
    q = deque()
    q.append(N)
    dp = [100001] * 100001
    dp[N] = 0
    while q:
        i = q.popleft()
        if i == M:
            print(dp[i])
            return
        next_list = [i + A,i + B,i + 1,i - 1,i - A,i - B,i * A,i * B]
        for nl in next_list:
            if not(0 <= nl < 100001) or dp[nl] != 100001:
                continue
            if dp[nl] < dp[i]+1:
                continue
            dp[nl] = dp[i]+1
            q.append(nl)



A, B, N, M = map(int, input().split())
bfs()
#
# for i in range(100001):
#     plus_A = i + A
#     plus_B = i + B
#     plus_1 = i+1
#     minus_1 = i-1
#     minus_A = i-A
#     minus_B = i-B
#     mux_A = i * A
#     mux_B = i * B
#     if 0 <= plus_A < 100001:
#         dp[plus_A] = min(dp[plus_A], dp[i] + 1)
#     if 0 <= plus_B < 100001:
#         dp[plus_B] = min(dp[plus_B], dp[i] + 1)
#     if 0 <= plus_1 < 100001:
#         dp[plus_1] = min(dp[plus_1], dp[i] + 1)
#     if 0 <= minus_1 < 100001:
#         dp[minus_1] = min(dp[minus_1], dp[i] + 1)
#     if 0 <= minus_A < 100001:
#         dp[minus_A] = min(dp[minus_A], dp[i] + 1)
#     if 0 <= minus_B < 100001:
#         dp[minus_B] = min(dp[minus_B], dp[i] + 1)
#     if 0 <= mux_A < 100001:
#         dp[mux_A] = min(dp[mux_A], dp[i] + 1)
#     if 0 <= mux_B < 100001:
#         dp[mux_B] = min(dp[mux_B], dp[i] + 1)
#
# print(dp[M])
