t = int(input())
for tc in range(t):
    N, *arr = map(int,input().split())
    arr.sort()

    res = 0
    # S(2) ~ S(N)
    for i in range(2,N+1):
        s = 0
        # 0~i 합
        for j in range(i):
            s += arr[j]
        # 해당 범위중 가장 큰 값에
        # 고른 M개를 곱한 것에서 원래 빌린돈을 빼서 차액을 구함
        min_s = arr[i-1]*i - s

        for j in range(i,N):
            s = s + arr[j] - arr[j-i]
            if min_s >= arr[j] * i - s:
                min_s = arr[j] * i - s
        res += min_s
    print(res)
