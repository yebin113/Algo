from sys import stdin
from collections import deque

# M개의 우주, N개의 행성 개수
M, N = map(int, stdin.readline().split())
universe = deque()
set_uni = deque()
check_idx = [0] * M
# M개의 우주
for _ in range(M):
    # 원래의 우주
    arr = list(map(int, stdin.readline().split()))
    # 정렬시키고 축소 시킨 우주(같은거 삭제)
    set_arr = sorted(list(set(arr)))
    # 시간 단축을 위해 딕셔너리 사용
    rank = {set_arr[i] : i for i in range(len(set_arr))}
    count_uni = [rank[arr[i]] for i in range(N)]

    if count_uni not in set_uni:
        set_uni.append(count_uni)
        check_idx[set_uni.index(count_uni)] += 1
    # 있는 우주는 체크(쌍체크)
    else:
        check_idx[set_uni.index(count_uni)] += 1

ans = 0

for i in range(len(set_uni)):
    if check_idx[i] == 1:
        continue
    ans += (check_idx[i]*(check_idx[i]-1))//2
print(ans)
