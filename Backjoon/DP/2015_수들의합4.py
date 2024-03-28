N,M = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()
cnt = 0

start = 0
end = 1
while start < N and end < N:
    hap = arr[end] + arr[start]
    # print("start",start, "arr[start]",arr[start],"end",end, "arr[end]",arr[end],"hap",hap)
    # 합이 M일때 답 + 1
    if hap == M:
        cnt += 1
        end += 1
        if end == N:
            start += 1
            end = start + 1
    elif hap < M:
        end += 1

        if end == N:
            start += 1
            end = start + 1

    else:
        start += 1
        end = start + 1
        continue

print(cnt)