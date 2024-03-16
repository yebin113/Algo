import sys
from collections import deque

"""
물 옮기는 방법
A -> B
B -> A
B -> C
C -> B
A -> C
C -> A
"""


def bfs():
    q = deque()
    visited = [[0] * (B + 1) for _ in range(A + 1)]
    # 가장 처음 상태
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        a, b = q.popleft()
        c = total_water - (a + b)
        # a가 비었을때, c의 양 추가
        if a == 0:
            amount.append(c)
        # A -> B, B -> A, B -> C, C -> B, A -> C, C -> A
        # a -> b
        cases = [[a - min(a, B - b), b + min(a, B - b)], [a - min(a, C - c), b], [a + min(b, A - a), b - min(b, A - a)],
                 [a, b - min(b, C - c)], [a + min(c, A - a), b], [a, b + min(c, B - b)]]
        for i, j in cases:
            if not visited[i][j]:
                visited[i][j] = True
                q.append((i, j))
        # print(q)


A, B, C = map(int, input().split())
# 총 물 양
total_water = C
amount = []
bfs()
print(*sorted(amount))