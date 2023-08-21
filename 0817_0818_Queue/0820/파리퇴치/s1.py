import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())

    arr = [list(map(int,input().split())) for i in range(N)]


    # 최대 파리 죽인 수
    max_kill = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 지금 당장 죽인 파리 수
            kill = 0
            for k in range(i, i+M):
                for m in range(j, j+M):
                    kill += arr[k][m]
            # 최댓값 갱신
            if max_kill < kill:
                max_kill = kill

    print(f'#{tc} {max_kill}')
