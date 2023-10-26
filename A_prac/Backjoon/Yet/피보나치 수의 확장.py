N = int(input())
check = False
if N == 0:
    print(0)
    print(0)
else:
    dp = [0] * 1000001
    if N < 0:
        N = -N
        check = True

        dp[0] = 0
        dp[1] = 1
        dp[2] = -1
        if N >= 3:
            for i in range(3, N + 1):
                # print(dp[i-2],dp[i-1])
                if dp[i - 2] - dp[i - 1] < 0:

                    dp[i] = - (abs(dp[i - 2] - dp[i - 1]) % 1000000000)
                else:
                    dp[i] = abs(dp[i - 2] - dp[i - 1]) % 1000000000
    else:
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        if N >= 3:
            for i in range(3, N + 1):
                dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000
    # print(dp[:N+1])
    if dp[N] < 0:
        print(-1)
        print(-dp[N])
    elif dp[N] == 0:
        print(0)
        print(0)
    else:
        print(1)
        print(dp[N])
