N = int(input())
numbers = list(map(int, input().split()))

dp = [1] * N
dp[0] = numbers[0]
for i in range(1, N):
    for j in range(i):
        # 증가하면 현재 수 + 지금 수 와 지금 값 갱신
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + numbers[i])
        # 증가 안하면 이전 수와 현재값 갱신
        else:
            dp[i] = max(dp[i], numbers[i])

print(max(dp))
