"""
종이 꽃가루가 들어있는 풍선이 M개씩 N개의 줄에 붙어있고, 어떤 풍선을 터뜨리면 안에 든 종이 꽃가루 개수만큼
상하 좌우의 풍선이 추가로 터지게 되는 게임이 있다.

예를 들어 풍선에 든 꽃가루가 1개씩일 때, 가운데 풍선을 터뜨리면 상하좌우의
풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.
"""

"""
for i 0 -> N-1
    for j 0 -> N-1
        cnt = arr[i][j]
        for k :0->3     
            for     # k 방향으로 확인하는 개수
"""
import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    max_sum_plus = 0

    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    for i in range(N):
        for j in range(M):
            sum_plus = arr[i][j]    # 현재위치부터 더함
            for k in range(4):      # 4방향 더할때 사용하는 반복(인접)
                ni = di[k] + i      # 해당 위치에서 어떤 방향으로 갈지 인접 인덱스 재정의
                nj = dj[k] + j
                if 0 <= ni < N and 0 <= nj < M:     # 벽세우기
                    sum_plus += arr[ni][nj]     # 더하기
            if max_sum_plus < sum_plus:     # 최댓값
                max_sum_plus = sum_plus

    print(f'#{tc} {max_sum_plus}')
