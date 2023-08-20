import sys
sys.stdin = open("input.txt")

T = int(input())
di = [0,0,-1,1]
dj = [-1,1,0,0]
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for i in range(N)]
    max_pang = 0
    for i in range(N):
        for j in range(M):
            sum_pang = arr[i][j]
            for k in range(4):
                for m in range(1,arr[i][j]+1):
                    # 새로운 위치
                    ni = i +di[k] * m
                    nj = j +dj[k] * m
                    # 벽세우기
                    if 0 <= ni < N and 0 <= nj < M:
                        # 해당 위치의 풍선의 값만큼 터진것을 더함
                        sum_pang += arr[ni][nj]
            # 최댓값 갱신
            if max_pang < sum_pang:
                max_pang = sum_pang

    print(f'#{tc} {max_pang}')