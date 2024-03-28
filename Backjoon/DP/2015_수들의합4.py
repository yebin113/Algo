N, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))

dp = [0]

# 누적합
for i in range(1, N + 1):
    dp.append(dp[i - 1] + arr[i])
# 딕셔너리 저장
num_dict = {}
answer = 0
# 배열을 돌아가면서
for i in range(N + 1):
    # dp[i] - K 값이 num_dict에 존재하는 경우 answer에 더함
    answer += num_dict.get(dp[i] - K, 0)
    # dp[i] 값을 num_dict에 저장
    num_dict[dp[i]] = num_dict.get(dp[i], 0) + 1
print(answer)