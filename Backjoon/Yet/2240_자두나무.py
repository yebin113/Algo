import sys
input = sys.stdin.readline

T,W = map(int, input().split())

tree = [0]
for _ in range(T):
    tree.append(int(input()))

dp = [[0] * (W+1) for _ in range(T+1)]

# 이동 횟수 홀수 -> 2번 나무 아래,
# 짝수면 1번 나무 아래
dp[1][0] = tree[1] % 2
dp[1][1] = tree[1] // 2
for t in range(2, T + 1):
    for w in range(W + 1):
        if w % 2 == 0:
            j = tree[t] % 2
        else:
            j = tree[t] // 2
        # 1초전에 얻는 최대 자두 개수 + 이동한 위치에서 얻는 자두 개수
        dp[t][w] = max(dp[t - 1][0:w + 1]) + j
print(max(dp[-1]))