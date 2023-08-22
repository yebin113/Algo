import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    # 두칸씩 뛰면서 검사
    for i in range(0,N,2):
        max_idx = i
        min_idx = i+1
        # i 부터 끝까지 검사
        for j in range(i,N):
            # 최댓값 인덱스 구하기
            if arr[max_idx] < arr[j]:
                max_idx = j
        # 바꾸기
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        for j in range(i, N):
            # 최솟값 인덱스 구하기
            if arr[min_idx] > arr[j]:
                min_idx = j
        # 바꾸기..
        arr[i + 1], arr[min_idx] = arr[min_idx], arr[i + 1]

    # 10개 넘으면 10개만 출력하는거 조건 까먹고 많이 틀림
    print(f'#{tc}',*arr[:10])