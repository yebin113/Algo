import math
N, M, L = map(int, input().split())
where = [0] + list(map(int, input().split())) + [L]
where.sort()

distance = [where[1]]+[0]*N
for i in range(1,N+1):
    distance[i] = where[i+1]-where[i]


start = 1
end = L-1
ans = 0
while start <= end:
    mid = (start+end)//2
    if mid == 0:
        continue
    count_h = 0
    for i in range(0,len(distance)):
        if distance[i] > mid:
            count_h += (distance[i] - 1)//mid
        # print(f'distance {distance[i]} mid {mid} 휴게소 {count_h} length {length}')

    # 만약 휴게소가 M개보다 덜 지어졌다면
    if count_h <= M:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1
    # print(f'start {start} end {end} mid {mid} ans {ans} 지어진 휴게소 {count_h}')
print(ans)

