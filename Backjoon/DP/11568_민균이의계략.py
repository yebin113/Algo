N = int(input())
cards = [0] + list(map(int,input().split()))
dp = [0 for _ in range(N + 1)]


for i in range(1, N + 1):
    for j in range(i):
        if cards[j] < cards[i]:
            dp[i] = max(dp[i], dp[j] + 1)
# print(dp)
print(max(dp))

# max_cnt = 1
# for i in range(N):
#     number = cards[i]
#     cnt = 1
#     for j in range(i+1,N):
#         print(i, number, j, cards[j])
#         if number >= cards[j]:
#             continue
#         cnt += 1
#         number = cards[j]
#         print(cnt)
#     max_cnt = max(max_cnt,cnt)
# print(max_cnt)