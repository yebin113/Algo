"""
각 수에서 1, 2, 3을 뺀 수에서 1가지 경우의 수씩 더함
"""
dp = [[0] * 1001 for _ in range(1001)]
MAX_NUM = 1000000009
dp[1][1] = dp[2][1] = dp[3][1] = 1
for i in range(2, 1001) :
    for j in range(1, 1001) :
        for k in range(3) :
            if j - k > 0 :
                dp[j][i] += dp[j - (k+1)][i - 1]
            dp[j][i] %= MAX_NUM
for _ in range(int(input())) :
    N, M = map(int, input().split())
    print(dp[N][M])