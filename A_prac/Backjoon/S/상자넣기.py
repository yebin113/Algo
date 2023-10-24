import sys
input = sys.stdin.readline
import math
import time

start = time.time()
math.factorial(100000)


def find(i,size,boxes):
    global max_box
    # print(f'i {i} size {size} boxes {boxes}')
    if i == N:
        max_box = max(max_box,boxes)
        return

    # 현재값보다 큰 값 찾으면
    for j in range(i+1,N+1):
        if size < arr[j]:
            dp[j] = dp[i] + 1
            find(j,arr[j],dp[j])

    else:
        max_box = max(max_box, boxes)
        return





N = int(input())
arr = list(map(int,input().split()))

dp = [1]*N
for i in range(N):
    now = arr[i]
    for j in range(i):
        left = arr[j]
        if left < now:
            dp[i] = max(dp[i],dp[j] + 1)
print(max(dp))




# end = time.time()
#
# print(f"{end - start:.5f} sec")