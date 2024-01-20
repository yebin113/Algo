"""
카드 팩의 가격이 주어졌을 때, N개의 카드를 구매하기 위해
민규가 지불해야 하는 금액의 최댓값을 구하는 프로그램
1~N 현재 dp[i]값과,
1~i까지의 카드팩가격 + dp[i-카드갯수] 합과 비교하여 갱신시켜줌

"""
N = int(input())
dp = [0]*(N+1)
p = [0] + list(map(int,input().split()))
for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i],dp[i-j]+p[j])
print(dp[N])
