N = int(input())
points = [[] for _ in range(N)]
for _ in range(N):
    x, y = map(int, input().split())
    points[y - 1].append(x)
cnt = 0
for point in points:
    point.sort()
    if len(point) <= 1:
        continue
    cnt += abs(point[0] - point[1]) + abs(point[-1] - point[-2])
    for j in range(1, len(point) - 1):
        cnt += min(abs(point[j] - point[j - 1]), abs(point[j] - point[j + 1]))
print(cnt)
