N = int(input())
arr = list(map(int,input().split()))
if N == 2:
    # 두개면 그냥 바로 더하기
    print(sum(arr))
elif arr[0] >= 0:
    # 0 이상부터 시작하면 앞의 두개
    print(arr[0]+arr[1])
elif arr[-1] <= 0:
    # 모두 음수면
    print(arr[-2]+arr[-1])
else:
    # 시작과 끝 인덱스
    start = 0
    end = N-1
    # 최소값 초기화
    min_hap = abs(arr[-1])+abs(arr[0])
    idx1 = start
    idx2 = end
    check_zero = False
    # start와 end 인덱스 중에 더 절대값이 큰 쪽을 줄임
    while start < end:
        if min_hap > abs(arr[start]+arr[end]):
            min_hap = abs(arr[start] + arr[end])
            idx1 = start
            idx2 = end
        if abs(arr[start]) < abs(arr[end]):
            end -= 1

        elif arr[start]+arr[end] == 0:
            min_hap = 0
            check_zero = True
            break
        else:
            start += 1
    if check_zero:
        print(0)
    else:
        print(arr[idx1]+arr[idx2])



