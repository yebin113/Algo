"""
5xS 2차 배열에 무작위로 25개의 숫자로 초기화 한 후
25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.
25개의 요소에 대해서 모두 조사하여 총합을 구하시오.
벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주의하시오.
예를 들어 [0][0]은 이웃한 요소가 2개이다.
"""

"""
수업시간에선 그냥 합..
"""
import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]  # 인접 배열 위치
    dj = [1, 0, -1, 0]

    max_v = 0  # 모든 원소가 0 이상이라면...

    for i in range(N):
        for j in range(N):  # 모든 원소 arr[i][j]에 대해
            s = arr[i][j]  # 일단 그 자리에 해당하는 요소를 합의 초기값을 설정
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:  # 유효한 인덱스면
                    s += arr[ni][nj]  # 주변 원소를 포함한 합

            if max_v < s:  # 총합 중 최댓값 구하기
                max_v = s
    print(f'#{tc}')
