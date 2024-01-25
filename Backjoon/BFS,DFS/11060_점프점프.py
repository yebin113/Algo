N = int(input())
arr = list(map(int, input().split()))
dp = [1001]*N
dp[0] = 0
# 0부터 N까지
for i in range(N):
    # 해당 위치 (+1~ 해당 위치 숫자)
    for di in range(1, arr[i]+1):
        ni = i + di
        #  범위 밖으로 나가면 나가기
        if ni >= N:
            break
        # 최소 갱신
        dp[ni] = min(dp[ni], dp[i]+1)
if dp[-1] != 1001:
    print(dp[-1])
else:
    print(-1)