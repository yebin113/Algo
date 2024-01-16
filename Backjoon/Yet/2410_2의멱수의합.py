
N = int(input())
dp = [0] * (N + 1)
dp[0] = 1

# 2의 제곱수 리스트를 만든다
twos = [2 ** k for k in range(21)]

for two in twos:
    if two <= N:
        for i in range(two, N + 1):
            dp[i] += (dp[i- two]) % 1000000000

print(dp[-1] % 1000000000)

# N = int(input())
# dp = [0] * (N + 1)
#
# NUM = 1000000000
# zegop = [2 ** i for i in range(21)]
# dp[0] = 1
#
# for z in zegop:
#     if z <= N:
#         for i in range(z, N + 1):
#             dp[i] += dp[i - z] % NUM
#
# print(dp[N] % 1000000000)
