# """
# 1. itemtools combination 사용시 메모리 초과 -> 조합 함수 만들기
# 2. comb 함수 생성 시간초과 -> 지금의 합이 집합 내 가장 큰 값보다 클때
#
# """
#
# import time
# start = time.time()
# #
# # import random
# # for i in range(200):
# #     print(random.randrange(1,2000000))
# #
# def comb(i, n, k, s):
#     global max_hap
#     if i >= n:
#         return
#     if s > max_num or (k == 1 and s + max_num < max_hap) and k == 0:
#         # print('조합 실패', s)
#         return
#     if k == 1 and s + set_arr[i] in set_arr:
#         max_hap = max(max_hap, s + set_arr[i])
#         return
#     else:
#         bit[i] = 1
#         comb(i + 1, n, k - 1, s + set_arr[i])
#         bit[i] = 0
#         comb(i + 1, n, k, s)
#
#
#
# max_num = max(set_arr)
# max_idx = set_arr.index(max_num)
#
# if max_idx != N - 1:
#     set_arr[-1], set_arr[max_idx] = set_arr[max_idx], set_arr[-1]
# max_hap = 0
# bit = [0] * (N)
#
# comb(0, N, 3, 0)
#
# print(max_hap)
# print("time :", time.time() - start)




from collections import deque
from sys import stdin
N = int(stdin.readline())
arr = [0] * N
for i in range(N):
    a = int(stdin.readline())
    arr[i] = a

sum_list = set()
for i in range(N-1):
    for j in range(N-1):
        sum_list.add(arr[i]+arr[j])

arr.sort()
in_sum = deque()
for i in range(N):
    for j in range(i+1,N):
        if i == j:
            continue
        if arr[j] - arr[i] in sum_list:
            in_sum.append(arr[j])
print(max(in_sum))