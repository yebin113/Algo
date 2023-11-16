import sys
N, C = map(int,sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()
max_length = arr[-1]-arr[0]
min_length = 1
ans = max_length
while min_length <= max_length:
    middle = (min_length+max_length)//2
    gong = 1
    start = arr[0]
    for i in range(N):
        if arr[i] >= middle + start:
            start = arr[i]
            gong += 1
    if gong >= C:
        min_length = middle + 1
        ans = middle
    else:
        max_length = middle - 1

print(ans)