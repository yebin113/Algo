import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    hap = 0
    min_list = []
    every_list = []
    # 첫줄은 가로줄 방문, 두번째줄은 세로줄 방문
    visited = [0]*N
    # 각 줄의 최소와 위치 구하기
    for i in range(N):
        # 인덱스와 값이 튜플형태로 들어있는 리스트
        idx_arr = list(enumerate(arr[i]))
        idx_arr.sort(key=lambda x:x[1])
        # 인덱스와 값이 튜플형태로 들어있는 리스트를 요소로 가지는 리스트
        # [[(,),(,)],[(,),(,)]]
        every_list.append(idx_arr)


    # # 최소 구하기...
    # if min_hap > hap:
    #     min_hap = hap


    # print(f'#{tc} {min_hap}')