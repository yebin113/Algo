cnt = 0


def fibo(n):
    global cnt

    cnt += 1
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

N = 30
memo = [0] * (N+1)


def fibomemo(n):
    global cnt
    global memo
    cnt += 1
    if n < 2:
        return memo[n]
    else:
        if memo[n] == 0:
            memo[n] = fibomemo(n-1) +fibo(n-2)
        return memo[n]


def fibodp(n):
    dp = [0] * n+1
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


print(fibodp(30))
