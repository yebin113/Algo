N, M = map(int, input().split())
N_arr = []

start = 0
end = 0
for _ in range(N):
    num = int(input())
    if num >= 0:
        end += num
    # else:
    #     start += num
    N_arr.append(num)


ans = 0
while start <= end:
    mid = (start + end) // 2
    chance = 0

    hap = 0
    for i in range(N):
        # 시작이 0이하면 ..
        if hap == 0 and N_arr[i] < 0:
            continue
        hap += N_arr[i]
        if hap >= mid:
            hap = 0
            chance += 1


    if chance < M:
        start = mid + 1
    elif chance > M:
        end = mid - 1
    else:
        start = mid + 1
        ans = mid

print(ans)