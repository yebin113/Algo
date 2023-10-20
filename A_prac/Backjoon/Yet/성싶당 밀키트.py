# N 개의 재료가 들어 있다.
# i 번째 재료의 유통기한은 밀키트를 구매한 후 L_i 일까지
# 부패 속도는 S_i
# x 일에 i 번째 재료에 있는 세균수 S_i*max(1,x-L_i)
# 모든 재료의 세균수의 합이 G마리 이하일 경우 안심
# 재료 K개 까지 빼서 세균수가 G 이하면 먹음
import sys

input = sys.stdin.readline
from collections import deque

N, G, K = map(int, input().split())
data = deque()
max_day = 0
for i in range(N):
    Si, Li, Oi = map(int, input().split())
    max_day = max(G//Si + Li, max_day)
    data.append([Si, Li, Oi])
# 각 재료의 세균 합을 구함
# 재료가 뺄수 있는지 없는지 판단
start = 0
end = max_day
ans = 0

