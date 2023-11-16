import sys
from collections import deque

n, m, k = list(map(int, sys.stdin.readline().split()))
arr = []
for u in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))
god_like = dict()


def bfs(i, j):
    queue = deque()
    queue.append((i, j, arr[i][j]))

    while queue:
        x, y, word = queue.popleft()

        if word not in god_like:
            god_like[word] = 1
        else:
            god_like[word] += 1

        if len(word) >= 5:
            continue

        for di, dj in [[0, 1], [-1, 0], [1, 0], [0, -1], [-1, 1], [-1, -1], [1, -1], [1, 1]]:
            ni = x + di
            nj = y + dj

            # 환형 처리
            if ni >= n:
                ni -= n
            if nj >= m:
                nj -= m
            if ni < 0:
                ni += n
            if nj < 0:
                nj += m

            queue.append((ni, nj, word + arr[ni][nj]))


answer = []

for i in range(n):
    for j in range(m):
        bfs(i, j)

for u in range(k):
    like = sys.stdin.readline().rstrip()

    if like in god_like:
        answer.append(god_like[like])
    else:
        answer.append(0)

for ans in answer:
    print(ans)