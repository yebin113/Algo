import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 1. 버블정렬
    # N 개의 숫자에 대해서 정렬해야함
    for k in range(N):
        # 뒤에서부터 앞으로 하나씩 오면서 비교
        for i in range(N - 1, -1, -1):
            # i번째 숫자와 그 후의 숫자들에 대해 비교를 함
            for j in range(i, N):
                # 앞이 더 크면 자리 바꾸기(오름차순)
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
    print(f'버블정렬 오름차순 #{tc}',*arr)

    # 2. 선택 정렬 ( 내림차순 )
    for i in range(N):
        # 최댓값을 각구간의 처음 수로 초기화
        max_num = arr[i]
        max_idx = i     # 현재의 인덱스도 저장해줘야 끝까지 작동
        # 그 후의 숫자들과 비교
        for j in range(i,N):
            # i~ N-1까지 최댓값을 갱신
            if max_num < arr[j]:
                max_num = arr[j]
                max_idx = j
        # 최댓값을 현재의 위치와 변경
        arr[max_idx],arr[i] = arr[i],arr[max_idx]



    print(f'선택정렬 내림차순 #{tc}',*arr)
