# 첫째 줄에 N이 주어진다.
# 다음 줄에는 N명의 학생들의 점수가 나이 순서대로 주어진다.
# 각 학생의 점수는 0 이상 10,000 이하의 정수이다.
N = int(input())
point = list(map(int, input().split()))
"""
10
2 5 7 1 3 4 8 6 9 3
"""
dp=[0]*(N)

start = 0
for i in range(1,N):
    max_num = point[i]
    min_num = point[i]
    for j in range(i,-1,-1):
        # i 번째부터 뒤로 돌아가면서 최대 최소와를 갱신
        # 원래 dp값과 1칸 전의 점수 + 현재 점수를 더하며 최대 갱신
        max_num = max(max_num,point[j])
        min_num = min(min_num, point[j])

        if j == 0:
            dp[i] = max(dp[i], max_num - min_num)
        else:
            dp[i] = max(dp[i], max_num - min_num + dp[j - 1])

print(dp[N-1])
