N, M, L = map(int, input().split())
where = list(map(int, input().split()))
where.sort()

max_length = where[-1] - where[0]
min_length = 1
ans = max_length
while min_length <= max_length:
    middle = (min_length + max_length) // 2
    rest = 1
    start = where[0]
    for i in range(N):
        if where[i] >= middle + start:
            start = where[i]
            rest += 1
    if rest >= L:
        min_length = middle + 1
        ans = middle
    else:
        max_length = middle - 1
print(ans)
