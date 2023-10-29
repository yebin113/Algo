import math

N = int(input())
line = [int(input()) for _ in range(N)]

cnt = 0
# 서로소의 크기만큼
dp = [0]*(max(line)+1)

# N개의 개수를 돌아가면서
for i in range(N):
    # 1부터 가장 큰수 까지
    for j in range(1,max(line)+1):
        # 만약 j번째 서로소가 0이 아니라면(계산x 부분)
        if dp[j] != 0:
            dp[math.gcd(j,line[i])]+= dp[j]
    # i번째에 개수 하나 더 추가
    dp[line[i]] += 1
print(dp[1]%10000003)