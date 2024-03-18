T = int(input())
LARGE_NUM = 1000000009
for _ in range(T):
    N,M = map(int,input().split())
    dp = [0] * (N+1)