n, k = map(int, input().split())
coin_values = []

for _ in range(n):
    coin_value = int(input())
    coin_values.append(coin_value)

# 각 동전의 가치를 만들 경우의 dp
#
dp = [0]*(k+1)
dp[0] = 1
for c in coin_values:
    for i in range(c,k+1):
        dp[i] += dp[i-c]
print(dp[k])