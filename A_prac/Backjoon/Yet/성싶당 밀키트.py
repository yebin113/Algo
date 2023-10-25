import sys
from collections import deque
from heapq import heappush,heappop

input = sys.stdin.readline

N, G, K = map(int, input().split())
data = deque()

for i in range(N):
    Si, Li, Oi = map(int, input().split())

    data.append([Si, Li, Oi])

start = 0
end = int(2e9)
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
        # 뺄수 있는 것들 (최대힙으로 저장)
        if K != 0:
            if O == 1:
                if len(germs_sort) < K:
                    heappush(germs_sort,germ)
                elif min(germs_sort) < germ:
                    heappush(germs_sort, germ)
    # print('plus',germs_sort)

    for i in range(len(germs_sort) - K):
        heappop(germs_sort)
    germ_hap -= sum(germs_sort)
    # 세균의 합이 G보다 작으면(조건 충족)
    if germ_hap < G:
        start = mid + 1
        ans = max(ans,mid)
    else:
        end = mid -1

print(ans)