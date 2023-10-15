from sys import stdin
from collections import deque

def is_not_same(arr1,arr2):
    if arr1 in arr2:
        return False,1
    arr1.sort()
    if arr1 in arr2:
        return False,2
    else:
        return True,3



# M개의 우주, N개의 행성 개수
M,N = map(int,stdin.readline().split())
universe = deque()
# M개의 우주
for _ in range(M):
    arr = list(map(int,stdin.readline().split()))
    set_arr = sorted(list(set(arr)))

    rank = {set_arr[i] :i for i in range(len(set_arr))}
    vector = tuple(rank[i] for i in arr)
    # count_uni = [0] * N
    # for i in range(N):
    #     count_uni[i] = set_arr.index(arr[i])+1
    # universe.append(count_uni)
    print(rank)

# set_uni = deque()
# check_idx=[0]*M
#
# for i in range(M):
#     if universe[i] not in set_uni:
#         set_uni.append(universe[i])
#         check_idx[set_uni.index(universe[i])] = 1
# print(universe,set_uni,check_idx)
# print(check_idx.count(1))
