import sys
input = sys.stdin.readline


def find(parents, x):
    # 부모 리턴
    if parents[x] != x:
        return find(parents, parents[x])
    return x


def union(parents, a, b):
    # a,b union
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

m, n = map(int, input().split())

parents = list(range(m + 1))

cnt = 0

for i in range(n):
    fr, to = map(int, input().split())
    # union 하기 전 사이클 확인
    if find(parents, fr) == find(parents, to):
        cnt += 1
    union(parents, fr, to)

connect = 0
for i in range(1, m):
    # 부모가 다를때 union해주고 연결 + 1
    if find(parents, i) != find(parents, i + 1):
        union(parents, i, i + 1)
        connect += 1

print(cnt + connect)