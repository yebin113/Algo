"""

다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을
작성하여라.

다음과 같은 5X5 배열에서 최댓값은 29이다.
"""

import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 저장할 변수
    max_sum = 0
    sum_left_to_right = 0
    sum_right_to_left = 0

    # 가로 합 구하기
    for i in range(100):    # 가로 행을 돌면서
        sum_row = 0         # 새로운 행이 될 때마다 각 행의 합을 0으로 초기화
        for j in range(100):    # 각 행의 요소를 순회하면서
            sum_row += arr[i][j]    # 행의 합을 구함
        if max_sum < sum_row:   # 그리고 만약 최댓값보다 지금 행의 합이 크다면
            max_sum = sum_row   # 변경합니다

    for j in range(100):        # 세로 열을 돌면서
        sum_col = 0     # 새로운 열이 될 때마다 각 열의 합을 0으로 초기화
        for i in range(100):        # 각 열의 요소를 순회하면서
            sum_col += arr[i][j]        # 열의 합을 구함
        if max_sum < sum_col:       # 그리고 만약 최댓값보다 지금 열의 합이 크다면
            max_sum = sum_col       # 변경합니다

    for i in range(100):        # 가로 행을 돌면서
        sum_left_to_right += arr[i][i]  # 대각선 1의 합
        sum_right_to_left += arr[i][99-i]   # 대각선 2의 합

    if max_sum < sum_left_to_right:   # 최댓값 갱신 여부
        max_sum = sum_left_to_right

    if max_sum < sum_right_to_left:  # 최댓값 갱신 여부
        max_sum = sum_right_to_left

    print(f'#{tc} {max_sum}')