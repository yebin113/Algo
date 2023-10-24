N, M, L = map(int, input().split())
where = [0] + list(map(int, input().split())) + [L]
where.sort()

distance = [where[1]]+[0]*N
for i in range(1,N+1):
    distance[i] = where[i+1]-where[i]

print(where)
print(distance)

start = 0
end = L
ans = L
while start <= end:
    mid = (start+end)//2
    count_h = 0
    max_length = 0
    location = 0
    i = 0
    while True:

        location += mid
        count_h += 1
        if location > distance[i]:
            count_h -= 1
            print(f'기존 휴게소 {distance[i]} 위치 {location} , 휴게소 {count_h}')
            location = 0
            i += 1
        if i == N+1:
            break

    if count_h <= M:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1
    print(f'start {start} end {end} mid {mid} ans {ans} 지어진 휴게소 {count_h}')
print(ans)

max_len = 0
for i in range(N+1):
    now_count = distance[i]%ans
    max_len = max(max_len,distance[i]//now_count)

print(max_len)
