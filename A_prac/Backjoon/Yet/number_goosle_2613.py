from sys import stdin

N,M = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))

# 숫자 하나로 이루어져 있다면
if arr.count(arr[0]) == N:
    if N % M == 0:
        print(arr[0] * (N // M))
    else:
        print(arr[0]*(N//M+1))
    for i in range(M):
        if i < N%M:
            print(N//M+1,end=' ')
        else:
            print(N//M,end=" ")
    print()
else:

    left = min(arr)
    right = 300*100
    ans = 0
    ans_p = 0
    min_max = 100*N
    while left <= right:
        middle = (left+right)//2
        # 일단 한 그룹 부터 시작
        group = 1
        # 그룹마다의 합을 구할 것
        hap = arr[0]
        max_hap = 0
        cnt = 0
        for i in range(N-1):
            if hap + arr[i+1] <= middle:
                hap += arr[i+1]

                max_hap = max(max_hap,hap)
            else:
                max_hap = max(max_hap, hap)
                hap = arr[i+1]
                group += 1
            # print(f'i: {i} middle: {middle} hap: {hap}, max_hap : {max_hap} group: {group}')

        if group > M:
            left = middle + 1

        else:
            right = middle -1
            min_max = min(min_max,max_hap)
            ans = middle
            ans_p = group
        # print(f'min_max: {min_max} max_hap: {max_hap}')

    cong_hap = [0]*ans_p
    count_cong = [0]*ans_p
    hap = 0
    j = 0
    hap = arr[0]

    for i in range(N - 1):
        if hap + arr[i + 1] <= ans:
            hap += arr[i + 1]
            cong_hap[j] = hap
        else:
            cong_hap[j] = hap
            count_cong[j] = i+1
            j += 1
            hap = arr[i + 1]

    count_cong[-1] = N
    # print(*count_cong)
    for i in range(ans_p-1,0,-1):
        count_cong[i] = count_cong[i] - count_cong[i-1]
    print(*cong_hap)
    print(min_max)
    print(*count_cong)
