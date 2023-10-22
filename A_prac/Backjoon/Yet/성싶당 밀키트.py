import sys
from collections import deque
from heapq import heappush,heappop

input = sys.stdin.readline

N, G, K = map(int, input().split())
data = deque()
max_day = 0
for i in range(N):
    Si, Li, Oi = map(int, input().split())
    max_day = max(G//Si + Li, max_day)
    data.append([Si, Li, Oi])

start = 0
end = max_day
ans = 0

while start <= end:
    mid = (start+end)//2
    germs_sort = []
    germ_hap = 0
    # 일단 다 더한다음 중요재료가 아닌 것들중
    # 가장 큰 K개만큼 뺌
    for i in range(N):
        S,L,O = data[i]
        germ = S * max(1,mid-L)
        germ_hap += germ
        # 뺄수 있는 것들
        if O == 1:

            heappush(germs_sort,(-germ,germ))
    # K개만큼 뺌
    for i in range(K):
        germ_hap -= heappop(germs_sort[1])

    # 세균의 합이 G보다 작으면(조건 충족)
    if germ_hap < G:
        start = mid + 1
        ans = max(ans,mid)
    else:
        end = mid -1

print(ans)