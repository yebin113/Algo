# import sys
#
# sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A_arr = list(map(int, input().split()))
    B_arr = list(map(int, input().split()))

    max_sum = 0

    # 짧은 배열과 긴배열을 선별
    if N > M:
        max_idx = N
        min_idx = M
        max_arr = A_arr
        min_arr = B_arr
    else:
        max_idx = M
        min_idx = N
        max_arr = B_arr
        min_arr = A_arr

    # 각 구간별 더하기를 실행할 횟수 =  큰 배열의 길이 - 작은 배열의 길이 + 1
    for i in range(max_idx - min_idx + 1):
        # 각 구간별 합 변수
        sum_arr = 0
        # 작은 배열의 길이만큼
        for j in range(min_idx):
            # 각 원소를 곱해서 더함
            sum_arr += max_arr[j + i] * min_arr[j]
        # 최댓값 갱신
        if max_sum < sum_arr:
            max_sum = sum_arr

    print(f'#{tc} {max_sum}')
