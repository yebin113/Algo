from sys import stdin

N, M = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

if N<M:
    print(N)
else:
    # 가장 적게 걸리는 시간
    start = 0
    # 가장 많이 걸리는 시간
    end = 60000000000
    ans = 0
    while start <= end:
        middle = (start + end) // 2
        # M명 채우고 시작
        people = M
        for i in range(M):
            people += middle//arr[i]
        # 만약 N명 보다 더 수용할 수 있으면
        if people >= N:
            # 시간이 덜걸림
            end = middle-1
            ans = middle
        # N명보다 적게 수용할 수 있는 시간이면
        else:
            # 시작을 늘림
            start = middle+1
        # 가장 나중에 탄 놀이기구 갱신

        # print(f'middle : {middle}, start: {start}, end:{end} people : {people}')

    ride = M
    # print(ans)
    # 1초 전까지 탑승한 모든 사람들
    for i in range(M):
        ride += (ans - 1)//arr[i]
    max_idx = 0
    # print("ride",ride)
    for i in range(M):
        # 만약 끝나는 시간에 딱 끝났다면
        if ans % arr[i] == 0:
            # 사람 추가
            ride += 1
        # N명이 된 순간끝
        if ride == N:
            max_idx = i
            # print("maxidx",max_idx)
            break
    print(max_idx+1)