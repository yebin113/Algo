import sys
input = sys.stdin.readline

word = ["B","O","J"]
n = int(input())
block = input()
dp = [int(1e9)] * n
dp[0] = 0
# dp 필요한 에너지의 최소값 저장
# 필요한 최소 에너지 양 갱신

for i in range(n):
    for j in range(i + 1, n):
        if dp[i] == -1:
            continue
        if word.index(block[j]) - word.index(block[i])== 1 or word.index(block[j]) - word.index(block[i])== -2:
            dp[j] = min(dp[i] + (j - i) ** 2, dp[j])

if dp[n - 1] == int(1e9):
    print(-1)
else:
    print(dp[n - 1])