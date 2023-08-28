import sys
sys.stdin = open("input.txt")


T = int(input())

for tc in range(1, T + 1):
    # 배열 크기와 스프레이 범위
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    max_v = 0
    for i in range(N):      # 스프레이를 뿌릴 위치
        for j in range(N):  # 스프레이를 뿌린 칸에서 처리되는 파리 수
            # + 방향
            s1 = arr[i][j]
            for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                for k in range(1,M):    # 각 방향으로 뿌릴 위치
                    ni,nj = i + di*k, j + dj*k
                    if 0 <= ni < N and 0 <= nj < N:
                        s1 += arr[ni][nj]
            # 최댓값 갱신
            if max_v < s1:
                max_v = s1
            # x 방향
            s2 = arr[i][j]
            for di,dj in [[1,1],[1,-1],[-1,-1],[-1,1]]:
                for k in range(1,M):    # 각 방향으로 뿌릴 위치
                    ni,nj = i + di*k, j + dj*k
                    if 0 <= ni < N and 0 <= nj < N:
                        s2 += arr[ni][nj]
            # 최댓값 갱신
            if max_v < s2:
                max_v = s2
    print(f'#{tc} {max_v}')
