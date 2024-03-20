N = int(input())
meeting = []
max_time = 0
for _ in range(N):
    start,finish,cnt = map(int,input().split())
    max_time = max(max_time,finish)
    meeting.append((start,finish,cnt))
# 회의 시작시간으로 정렬하기
meeting.sort()
dp = [0]*N
dp[0] = meeting[0][2]

# 회의시간은 양옆만 겹침 ->
# 1번째 전 vs 2번째 + 현재 인원수 중에 더 인원이 많은것을 지금에 저장해주면 됨
for i in range(1,N):
    dp[i] = max(dp[i-2]+meeting[i][2],dp[i-1])
print(dp[-1])




