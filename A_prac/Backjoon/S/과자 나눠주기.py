import sys
from collections import deque
# 조카의 수 M  과자의 수 N
M,N = map(int, sys.stdin.readline().split())
# 과자 N개의 길이 L1, L2, ..., LN
arr = list(map(int,sys.stdin.readline().split()))

# 조카가 과자수보다 적을때
if M<N:
    arr.sort()
    print(arr[N-1-M])
# 조카랑 과자수가 같을때
elif M==N:
    print(min(arr))
# 조카가 과자보다 많을때..
else:
    pass