"""
우선순위 큐를 사용
힙에서 가장 작은 두 숫자를 합쳐서 힙에 다시 삽입한다
가장 작은 두숫자들끼리 묶어둔 다음 더해가는 것이 가장 효율적
"""
import heapq
N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards,int(input()))
ans = 0
while len(cards) >1:
    i = heapq.heappop(cards)
    j = heapq.heappop(cards)
    sum_ij = i+j
    ans += sum_ij
    heapq.heappush(cards,sum_ij)

print(ans)

