import math
N, M, L = map(int, input().split())
where = [0] + list(map(int, input().split())) + [L]
where.sort()

distance = [where[1]]+[0]*N
for i in range(1,N+1):
    distance[i] = where[i+1]-where[i]

# print(where)
# print(distance)

start = 0
end = L
ans = L
while start <= end:
    mid = (start+end)//2
    count_h = 0
    max_length = 0
    for i in range(N+1):
        now_count = distance[i] // mid
        count_h += now_count
        length = distance[i]
        if now_count != 0:
            length = math.ceil(distance[i] / (now_count+1))
        max_length = max(max_length, length)
        # print(f'distance {distance[i]} mid {mid} 휴게소 {count_h} length {length}')

    # 만약 휴게소가 M개보다 덜 지어졌다면
    if count_h <= M:
        end = mid - 1
        ans = max_length
    else:
        start = mid + 1
    # print(f'start {start} end {end} mid {mid} ans {ans} 지어진 휴게소 {count_h}')
print(ans)

