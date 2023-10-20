N, M, L = map(int, input().split())
where = list(map(int, input().split()))
where.sort()

max_length = L
min_length = 1
ans = max_length

while min_length <= max_length:
    middle = (min_length + max_length) // 2
    rest = 0
    for i in range(N):
