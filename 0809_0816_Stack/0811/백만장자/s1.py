"""
    1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
    2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
    3. 판매는 얼마든지 할 수 있다.
"""
# 배열과 현재 인덱스를 주면 그 이후의 최댓값을 뽑아주는 함수
def choose_sort(arr,idx):
    max_price = 0
    for i in range(idx,len(arr)):
        if max_price< arr[i]:
            max_price = arr[i]
    return max_price

import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0


    # 배열을 순회하면서
    for i in range(N-1):
        if arr[i] < choose_sort(arr,i):
            # 최댓값 - 현재값 누적
            ans += choose_sort(arr,i) - arr[i]




    print(f'#{tc} {ans}')
