"""
5xS 2차 배열에 무작위로 25개의 숫자로 초기화 한 후
25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.
25개의 요소에 대해서 모두 조사하여 총합을 구하시오.
벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주의하시오.
예를 들어 [0][0]은 이웃한 요소가 2개이다.

"""
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]  # 인접 배열 위치
    dj = [1, 0, -1, 0]

    total = 0

    for i in range(N):
        for j in range(N):  # 모든 원소 arr[i][j]에 대해
            s = 0   # 각 요소의 상하좌우 절댓값 합은 새로운 요소를 마주할때마다 0으로 초기화 되어야함
            for k in range(4):
                ni = i + di[k]  # 인접한 인덱스
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:  # 유효한 인덱스면 - 0보다 작은 경우는 합 x

                    num = arr[ni][nj] - arr[i][j]   # 해당 요소와 인접한 인덱스 요소와의 차

                    if num > 0:     # 0보다 크면 그냥 더함
                        s += num
                    else:           # 0보다 작으면 빼고 더함(절댓값)
                        s -= num
            total += s

    print(f'#{tc} {total}')