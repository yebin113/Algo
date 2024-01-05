import heapq
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    K = int(input())
    size = list(map(int,input().split()))
    price = 0

    h = []

    for i in range(K):
        heapq.heappush(h,size[i])
    size = h
    while len(size) > 1:
        one = heapq.heappop(size)
        two = heapq.heappop(size)
        heapq.heappush(size,one+two)
        price += one+two
    print(price)
