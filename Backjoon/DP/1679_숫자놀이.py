N = int(input())
numbers = list(map(int,input().split()))
K = int(input())
dp = [[0]*2 for _ in range(N+1)]
print(dp[0])
print(dp[1])

# for _ in range(1,N+1):
