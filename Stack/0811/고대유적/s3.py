
import sys

sys.stdin = open("input.txt")
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    max_count = 0

    # 행 순회
    for i in range(N):
        count_one = 0
        for j in range(M):
            # 1을 만났을때
            if arr[i][j]:
                # count를 늘림
                count_one += 1

            # 0을 만났을때
            else:
                # count 초기화
                count_one = 0
            # for 돌때마다 최댓값 갱신
            if max_count < count_one:
                max_count = count_one
    # 열 순회
    for i in range(M):
        count_one = 0
        for j in range(N):
            # 1을 만났을때
            if arr[j][i]:
                # count를 늘림
                count_one += 1

            # 0을 만났을때
            else:
                # 초기화
                count_one = 0
            # 최댓값 갱신
            if max_count < count_one:
                max_count = count_one

    print(f'#{tc} {max_count}')